# %%
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer
import pymysql
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

def load_file(file_name):
    """
    Load a CSV file into a pandas DataFrame.
    Skips problematic lines during reading.
    """
    df = pd.read_csv(file_name, on_bad_lines='skip')
    return df

# %%
def convert_binary_columns(df, columns):
    """
    Convierte columnas binarias Yes/No a 1/0.
    """
    
    binary_map = {'Yes': 1, 'No': 0}
    
    for col in columns:
        df[col] = df[col].replace(binary_map).astype("Int64")
    return df

# %%
def remove_duplicates(df):
    """
    Elimina filas duplicadas y muestra cuántas se han eliminado.
    """
    initial_rows = len(df)
    
    df = df.drop_duplicates()
    
    final_rows = len(df)
    removed = initial_rows - final_rows
    
    print(f"Duplicados eliminados: {removed}")
    return df

# %%
def drop_columns(df, columns):
    """
    Elimina las columnas indicadas del DataFrame.
    
    Parametros:
    df (DataFrame): DataFrame original.
    columns (list): Lista de columnas a eliminar.
    """
    df = df.drop(columns=columns, errors="ignore")
    return df

# %%
def standardize_columns(df, title_columns=None, replacements=None):
    """
    Homogeneiza columnas de texto aplicando formato y reemplazos.
    
    Parameters:
    - title_columns (list): columnas a las que aplicar title() y strip()
    - replacements (dict): diccionario con {columna: {valor_antiguo: valor_nuevo}}
    """
    if title_columns:
        for col in title_columns:
            df[col] = df[col].str.title().str.strip()

    if replacements:
        for col, mapping in replacements.items():
            df[col] = df[col].replace(mapping)
    return df

# %%
def fill_with_mode(df, columns):
    """
    Rellena los nulos de las columnas indicadas con su moda.
    """
    for col in columns:
        df[col] = df[col].fillna(df[col].mode()[0])
    return df

# %%
def fill_with_value(df, columns, value):
    """
    Rellena los nulos de las columnas indicadas con un valor fijo.
    """
    for col in columns:
        df[col] = df[col].fillna(value)
    return df

# %%
def fill_with_median(df, columns):
    """
    Rellena los nulos de las columnas indicadas con la mediana.
    """
    for col in columns:
        df[col] = df[col].fillna(df[col].median())
    return df

# %%
def fill_with_iterative_imputer(df, columns, max_iter=100, random_state=42):
    """
    Aplica imputación iterativa a las columnas indicadas.
    """
    imputer = IterativeImputer(max_iter=max_iter, random_state=random_state)
    
    for col in columns:
        df[[col]] = imputer.fit_transform(df[[col]]).round()
    return df

# %%
def convert_column_types(df, column_types):
    """
    Convierte las columnas del DataFrame a los tipos indicados.
    """
    for col, dtype in column_types.items():
        if col in df.columns:
            df[col] = df[col].astype(dtype)
    return df

# %%
def create_income_band(df, source_column, new_column):
    """
    Crea una variable categórica basada en la media ± desviación estándar
    de la columna numérica indicada.
    
    Categorías:
    - Bajo: valor < media - std
    - Alto: valor > media + std
    - Medio: resto
    """
    
    mean = df[source_column].mean()
    std = df[source_column].std()
    
    def categorize(value):
        if value < mean - std:
            return "Low"
        elif value > mean + std:
            return "High"
        else:
            return "Medium"
    
    df[new_column] = df[source_column].apply(categorize)
    return df

# %%
def create_age_group(df, source_column, new_column):
    """
    Crea grupos de edad en rangos interpretables.
    """
    
    def categorize(age):
        if age < 25:
            return "Under 25"
        elif 25 <= age <= 45:
            return "25-45"
        else:
            return "Over 45"
    
    df[new_column] = df[source_column].apply(categorize)
    return df

# %%
def create_tenure_group(df, source_column, new_column):
    """
    Crea grupos de antigüedad en la empresa.
    """
    
    def categorize(years):
        if 0 <= years <= 2:
            return "0-2"
        elif 3 <= years <= 5:
            return "3-5"
        elif 6 <= years <= 9:
            return "6-9"
        else:
            return "10+"
    
    df[new_column] = df[source_column].apply(categorize)
    return df

# %%
def create_risk_score(df):
    """
    Calcula el RiskScore según el modelo definido
    en el análisis exploratorio.
    """
    
    df["RiskScore"] = (
        (df["JobSatisfaction"] <= 2).astype("Int64") * 2
        + df["OverTime"].astype("Int64") * 2
        + (df["IncomeBand"] == "Low").astype("Int64") * 1
        + (df["YearsAtCompany"] < 2).astype("Int64") * 1
        + (df["WorkLifeBalance"] <= 2).astype("Int64") * 2
        + (df["EnvironmentSatisfaction"] <= 2).astype("Int64") * 1
        + (df["RelationshipSatisfaction"] <= 2).astype("Int64") * 2
    )
    return df


# %%
def load_data(df):
    """
    Crea la conexión a la base de datos,
    divide el DataFrame en las tablas del modelo
    y realiza la carga en SQL.
    """

    load_dotenv()

    db_host = os.getenv("db_host")
    db_user = os.getenv("db_user")
    db_password = os.getenv("db_password")
    db_name = os.getenv("db_name")

    engine = create_engine(
        f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
    )


    employees_df = df[
        [
            "EmployeeNumber",
            "Age",
            "Gender",
            "MaritalStatus",
            "Education",
            "EducationField",
            "Department",
            "JobRole",
            "NumCompaniesWorked",
            "StockOptionLevel",
            "MonthlyIncome",
            "MonthlyRate"
        ]
    ].copy()

    employment_history_df = df[
        [
            "EmployeeNumber",
            "TotalWorkingYears",
            "YearsAtCompany",
            "YearsInCurrentRole",
            "YearsSinceLastPromotion",
            "YearsWithCurrManager",
            "BusinessTravel",
            "OverTime",
            "DistanceFromHome"
        ]
    ].copy()

    satisfaction_scores_df = df[
        [
            "EmployeeNumber",
            "JobSatisfaction",
            "EnvironmentSatisfaction",
            "RelationshipSatisfaction",
            "WorkLifeBalance",
            "JobInvolvement",
            "PerformanceRating"
        ]
    ].copy()

    attrition_risk_df = df[
        [
            "EmployeeNumber",
            "Attrition",
            "RiskScore",
            "IncomeBand",
            "TenureGroup",
            "AgeGroup"
        ]
    ].copy()

    employees_df.to_sql("employees", engine, if_exists="replace", index=False)
    employment_history_df.to_sql("employment_history", engine, if_exists="replace", index=False)
    satisfaction_scores_df.to_sql("satisfaction_scores", engine, if_exists="replace", index=False)
    attrition_risk_df.to_sql("attrition_risk", engine, if_exists="replace", index=False)


    print("Datos cargados correctamente en la base de datos.")

# %%
def run_etl():
    """
    Ejecuta el proceso completo ETL:
    Extract → Transform → Load
    """

    print("Iniciando proceso ETL...")

    df = load_file("hr.csv")

    df = convert_binary_columns(df, ["OverTime", "Attrition"])

    df = remove_duplicates(df)

    columns_to_drop = ["Over18", "EmployeeCount", "StandardHours"]

    df = drop_columns(df, columns_to_drop)
    
    title_columns = ["JobRole"]
    replacements = {
        "MaritalStatus": {"Marreid": "Married"},
        "BusinessTravel": {
            "Travel_Frequently": "Frequently",
            "Travel_Rarely": "Rarely",
            "Non-Travel": "Non-Travel"
        }
    }

    df = standardize_columns(df, title_columns, replacements)

    df = fill_with_mode(df, ["BusinessTravel", "Department"])
    df = fill_with_value(df, ["EducationField", "MaritalStatus"], "Unknown")
    df = fill_with_median(df, ["Age", "JobSatisfaction", "MonthlyIncome", "OverTime"])
    df = fill_with_iterative_imputer(df, ["TrainingTimesLastYear", "YearsWithCurrManager"])

    column_types = {
        "JobSatisfaction": int,
        "Age": int,
        "YearsWithCurrManager": int,
        "TrainingTimesLastYear": int,
        "MonthlyRate": float
    }

    df = convert_column_types(df, column_types)

    df = create_income_band(df, "MonthlyIncome", "IncomeBand")
    df = create_age_group(df, "Age", "AgeGroup")
    df = create_tenure_group(df, "YearsAtCompany", "TenureGroup")
    df = create_risk_score(df)

    load_data(df)

    print("Proceso ETL completado correctamente.")



