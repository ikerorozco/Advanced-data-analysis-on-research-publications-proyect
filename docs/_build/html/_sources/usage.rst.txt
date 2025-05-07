Uso del Proyecto
================

📁 **Estructura del Proyecto**
------------------------------
La estructura de archivos del repositorio es la siguiente:

.. code-block::

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

Para ejecutar el análisis, sigue las instrucciones de instalación y configuración.
