[![DOI](https://zenodo.org/badge/927833777.svg)](https://doi.org/10.5281/zenodo.14968794)
# 📝 Análisis de Artículos Científicos con Grobid


📖 **Documentación disponible en**: [ReadTheDocs](https://articlesanalysisgrobid.readthedocs.io/es/latest/)

Este repositorio contiene un pipeline de procesamiento de artículos científicos en **PDF**, utilizando **Grobid** para la extracción de datos y herramientas de visualización en **Python**.  

## 🚀 Objetivos del Proyecto  
El programa realiza los siguientes análisis sobre **artículos de acceso abierto**:  
1. **📌 Nube de palabras** basada en los resúmenes (**abstracts**).  
2. **📊 Gráfico** con el número de figuras por artículo.  
3. **🔗 Lista de enlaces** extraídos de cada documento.  

---

## 📁 Estructura del Proyecto  
```sh
├── data/                  # 📂 PDFs de entrada para su procesamiento  
├── output/                # 📂 Resultados generados (XMLs, gráficos, JSONs)  
│   ├── wordcloud.png      # 📊 Nube de palabras basada en los abstracts  
│   ├── figures_per_paper.png # 📈 Número de figuras por artículo  
│   ├── links_per_paper.json  # 🔗 Lista de enlaces extraídos  
├── src/                   # 📂 Código fuente del pipeline  
│   ├── config.py          # ⚙️ Configuración del entorno y rutas  
│   ├── extraction.py      # 🔍 Extracción de abstracts, figuras y enlaces  
│   ├── process.py         # 🛠️ Envío de PDFs a Grobid y procesamiento  
│   ├── visualization.py   # 📊 Generación de gráficos y visualizaciones  
│   ├── main.py            # 🚀 Script principal del programa  
├── Dockerfile             # 🐳 Configuración de contenedor para la aplicación  
├── docker-compose.yml     # 🐳 Configuración de servicios (Grobid + App)  
├── requirements.txt       # 📦 Dependencias necesarias  
├── rationale.md           # 📝 Validación de los resultados obtenidos  
├── LICENSE                # ⚖️ Licencia del proyecto  
└── README.md              # 📖 Documentación del repositorio  
```


# Instalación y Configuración

Existen dos métodos para ejecutar la aplicación:

1️⃣ **Usando Docker Compose (Recomendado)** – Corre Grobid y la aplicación en contenedores automáticamente.  
2️⃣ **Usando Python 3.10+ y un entorno virtual** – Ejecuta la aplicación sin Docker, pero usa **Grobid en un contenedor Docker**.

Ambos métodos permiten procesar los artículos y generar las visualizaciones automáticamente.

---

## 1️⃣ Método 1: Usando Docker Compose (Recomendado)

Este método inicia **Grobid y la aplicación** en contenedores separados, lo que facilita la ejecución sin instalar dependencias manualmente.

### **Paso 1: Clonar el repositorio**
```bash
git clone https://github.com/SergonM/ArticlesAnalysisGrobid.git
cd ArticlesAnalysisGrobid
```

### **Paso 2: Agregar los artículos en la carpeta `data/`**
- En la carpeta `data/` hay **2 artículos en PDF** por defecto.
- Puedes reemplazarlos o agregar nuevos documentos en esta carpeta.

### **Paso 3: Iniciar los servicios con Docker Compose**
Ejecuta el siguiente comando para levantar los servicios (en versiones de Docker antiguas es docker-compose):

```bash
docker compose up -d
```

🔹 Esto iniciará:  
- **Grobid** en `http://localhost:8070`  
- **La aplicación**, que interactúa con Grobid y procesa los artículos  

📌 **Notas**:
- Si Grobid no responde, verifica que el servicio esté activo en `http://localhost:8070/api/isalive`.
- Para detener los servicios:

```bash
docker compose down
```

---

## 2️⃣ Método 2: Usando Python 3.10+ con Virtualenv y Docker para Grobid

Este método usa **Python 3.10+** para ejecutar la aplicación y un contenedor **Docker para Grobid**.

### **Paso 1: Clonar el repositorio**
```bash
git clone https://github.com/SergonM/ArticlesAnalysisGrobid.git
cd ArticlesAnalysisGrobid
```

### **Paso 2: Crear y activar un entorno virtual**
Ejecuta los siguientes comandos para crear un entorno virtual en Python:

```bash
python -m venv venv
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate     # En Windows
```

### **Paso 3: Instalar las dependencias**
```bash
pip install -r requirements.txt
```

### **Paso 4: Agregar los artículos en la carpeta `data/`**
- En la carpeta `data/` hay **2 artículos en PDF** por defecto.
- Puedes reemplazarlos o agregar nuevos documentos en esta carpeta.

### **Paso 5: Iniciar Grobid con Docker**
Ejecuta el siguiente comando para iniciar **Grobid** en un contenedor **Docker**:

```bash
docker run -t --rm -p 8070:8070 -e JAVA_TOOL_OPTIONS=-XX:-UseContainerSupport lfoppiano/grobid:0.8.1
```

🔹 Esto iniciará **Grobid en `http://localhost:8070`**.  
🔹 Deja esta terminal abierta mientras se ejecuta Grobid.

### **Paso 6: Ejecutar la aplicación manualmente**
En otra terminal, asegúrate de que el entorno virtual sigue activado y ejecuta:

```bash
python src/main.py
```

📌 **Notas**:
- Grobid debe estar corriendo antes de ejecutar la aplicación.
- Si Grobid deja de responder, reinicia el contenedor con el **Paso 5**.

Ambos métodos permiten procesar los artículos y generar las visualizaciones automáticamente. 🚀

---

## 📊 Resultados Esperados  
Después de ejecutar el análisis, los resultados estarán en la carpeta `output/`:

| Archivo | Descripción |
|---------|------------|
| **`wordcloud.png`** | Nube de palabras con los términos más frecuentes en los resúmenes |
| **`figures_per_paper.png`** | Gráfico con la cantidad de figuras por artículo |
| **`links_per_paper.json`** | Lista de enlaces externos extraídos de los artículos |

---

## 📄 Validación de Resultados  
Para más detalles sobre la validación de los resultados, consulta el archivo [`rationale.md`](rationale.md).  

---

## 📜 Licencia
Este proyecto está bajo la licencia **GNU General Public License v3.0**.  

---

### 🔗 Referencias  
- [Grobid GitHub](https://github.com/kermitt2/grobid)  
- [Documentación de WordCloud](https://github.com/amueller/word_cloud)  
- [Docker Compose](https://docs.docker.com/compose/)  
