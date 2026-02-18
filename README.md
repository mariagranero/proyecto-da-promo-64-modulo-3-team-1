# 🧠 Proyecto Módulo 3 – Retención de Talentos

## Optimización de Talento y Análisis de Rotación de Empleados

Proyecto de análisis de datos de Recursos Humanos desarrollado en el marco del **Módulo 3** del bootcamp de **Adalab**.  
El objetivo del proyecto es analizar los factores que influyen en la **satisfacción laboral y la rotación de empleados**, utilizando técnicas de **análisis exploratorio de datos, transformación, visualización y diseño de bases de datos**.

La empresa ficticia **Mupa Healthcare** nos contrata para identificar patrones clave que ayuden a **reducir la rotación y mejorar la retención del talento**.

---

## 🏢 ¿Quién es Mupa Healthcare?

**Mupa Healthcare**, es una compañía líder en el Reino Unido especializada en salud y bienestar, fundada en 1985.  
La empresa ofrece seguros de salud, gestión hospitalaria, clínicas dentales y residencias de mayores, destacándose por un modelo de atención integral y digital que busca mejorar la experiencia y el cuidado de sus pacientes.

---

## 👥 Equipo y Roles

| Miembro | Rol | Tareas principales |
|------|-----|------------------|
| Ana María Castro | Risk Specialist | EDA, limpieza y transformación, feature engineering, análisis, indicadores de riesgo, visualizaciones |
| Camila López | Data Analyst | EDA, limpieza y transformación, análisis descriptivo, diseño BBDD y soporte ETL, visualizaciones |
| María Granero | Scrum Master | EDA, análisis descriptivo, coordinación del equipo, análisis, documentación, storytelling de negocio, validación de insights |

---

## 🎯 Objetivo del proyecto

Analizar los datos de empleados de **Mupa Healthcare** para identificar los factores que influyen en la **rotación (Attrition)** y la **satisfacción laboral**, con el fin de apoyar la toma de decisiones estratégicas en RRHH.

### Objetivos específicos
- Analizar la **rotación de empleados** y su relación con variables clave.  
- Identificar factores asociados a **alto riesgo de abandono**. 
- Evaluar satisfacción laboral, entorno y equilibrio vida-trabajo. 
- Crear **indicadores de riesgo** para anticipar la rotación.  
- Proponer métricas accionables para la optimización del talento.  

---

## 🔄 Flujo general del proyecto

1. Carga y exploración del dataset de empleados.  
2. Análisis exploratorio de datos (**EDA**) para comprender estructura y calidad.  
3. Limpieza, normalización y transformación de variables.  
4. Creación de nuevas métricas e indicadores (feature engineering).  
5. Visualización de insights clave para negocio.  
6. Diseño de la estructura de la base de datos relacional.  
7. (Bonus) Desarrollo de una **ETL** para automatizar el proceso.  

---

## 🧠 Tecnologías y contenidos aplicados

### Python
- Manipulación de datos con **pandas** y **numpy**.
- Análisis exploratorio de datos (EDA).
- Funciones personalizadas para categorización.
- Feature engineering.
- Exportación de datasets finales a CSV.

### Visualización
- Visualizaciones con **matplotlib** y **seaborn**.
- Análisis descriptivo orientado a RRHH.
- Storytelling de datos para negocio.

### Bases de datos
- Inserción de datos desde Python y creación automática de la estructura en MYSQLWorkbench.
- Definición de la estructura en la ETL mediante una función.

---

## 📒 Organización del código


### Notebooks

- **01_EDA.ipynb**  
  Exploración inicial: tipos, nulos, duplicados, estadística descriptiva.

- **02_Limpieza_transformación.ipynb**  
  Normalización, limpieza de variables y preparación del dataset.

- **03_Análisis.ipynb**  
  Feature engineering, creación de indicadores y análisis de rotación.

- **04_Visualizaciones.ipynb**  
  Gráficos clave: salario por departamento, riesgo por puesto, etc.


### Data

- Csv´s cargados: df_hr_clean.csv/ hr.csv

---

### Scripts ETL (Bonus)

Ubicados en la carpeta `ETL/`:

- `funciones.py`: funciones de extracción y transformación, así como de la creación de la base de datos y carga en carga en MySQL Workbench.  
- `main.py`: ejecución del pipeline completo.  
- Inserción automatizada en base de datos


---

## 🗂️ Estructura del repositorio
```text
proyecto-da-promo-64-modulo-3-team-1/
│
├── data/
│ ├── hr.csv
│ └── df_hr_clean.csv
│
├── ETL/
│ ├── pycache/
│ ├── .env.example
│ ├── .gitignore
│ ├── funciones.py
│ └── main.py
│
├── Notebooks/
│ ├── 01_EDA.ipynb
│ ├── 02_Limpieza_transformación.ipynb
│ ├── 03_Análisis.ipynb
│ └── 04_Visualizaciones.ipynb
│
├── README.md
└── requirements.txt
```
---

## ▶️ Pasos para configurar

### 1. Requisitos
- Python 3.9+
- Librerías principales:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`

---

### 2. Instalación y ejecución

#### Opción 1 – Ejecutar todo desde cero

1. Clonar el repositorio:

git clone https://github.com/mariagranero/proyecto-da-promo-64-modulo-3-team-1.git
cd proyecto-da-promo-64-modulo-3-team-1

2. Crear entorno virtual e instalar dependencias:

### Crear y activar entorno virtual, instalar dependencias

```
# Crear entorno virtual
python -m venv venv

# Activar entorno
# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```


3. Ejecución del análisis:

   - `01_EDA.ipynb`
   - `02_Limpieza_transformación.ipynb`
   - `03_Análisis.ipynb`
   - `04_Visualizaciones.ipynb`

4. Ejecutar todas las celdas para reproducir el análisis completo.


#### Opción 2 – Usar dataset final limpio

1. Cargar directamente el archivo `df_hr_clean.csv`.
2. Explorar las visualizaciones e indicadores ya creados.
3. Analizar el `RiskScore` y la rotación de empleados.


#### Opción 3 – Ejecutar pipeline ETL

Desde la carpeta ETL/, ejecutar:
`python main.py`

Este script realiza automáticamente:

- Extracción de datos.

- Transformación.

- Creación de tablas.

- Carga en la base de datos.

---

## 🧪 Pruebas y control de calidad

| Escenario | Manejo |
|---------|--------|
| Valores nulos | Identificación y control mediante EDA |
| Tipos incorrectos | Conversión explícita de tipos |
| Duplicados | Eliminación de filas duplicadas |
| Errores categóricos | Normalización de texto |
| Variables irrelevantes | Eliminación de columnas sin valor analítico |

---

## 🚀 Posibles mejoras futuras

- Creación de modelos predictivos de rotación.  
- Visualizaciones interactivas (Tableau / Power BI).  
- Segmentación avanzada de empleados.  
- Validación del `RiskScore` con modelos de ML.  

---

## 🎤 Presentación del proyecto

La presentación incluye:
- Contexto empresarial y objetivos.  
- Proceso de análisis de datos.  
- Visualizaciones clave. 
- Indicadores de riesgo de rotación.  
- Recomendaciones para RRHH.  

---

## 📄 Licencia

Proyecto académico desarrollado en el marco del bootcamp de **Adalab**.  
Uso educativo.

---

## 👩‍💻 Autoras

Este trabajo ha sido realizado de forma colaborativa por:

- **Ana María Castro**
- **Camila López**
- **María Granero**



Aquí sus redes sociales:

* **Ana María Castro Narciandi**
  * [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ana-maria-castro-narciandi/)
  * [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Narciandi90)

* **Camila López**
  * [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/camila-adriana-lopez-martin)
  * [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/camilalopezmrt)

* **María Granero**
  * [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mar%C3%ADa-granero-l%C3%B3pez/)
  * [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/mariagranero)





