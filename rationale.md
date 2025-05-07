# rationale.md

# **Justificación y Validación del Análisis con Grobid**  

## **1. Introducción**  
Este documento proporciona una justificación del enfoque utilizado para procesar y analizar 10 artículos de acceso abierto mediante **Grobid**. Se detallan las decisiones metodológicas, las pruebas realizadas y la validación manual de los resultados obtenidos.  

## **2. Metodología**  

### **2.1. Pipeline con Grobid y Selección Inicial de los Artículos**  
Se diseñó un pipeline automatizado que procesa documentos en PDF utilizando **Grobid**, una herramienta de extracción de datos estructurados en XML basada en modelos de aprendizaje automático.  

Los pasos del procesamiento son los siguientes:  
1. **Subida de los documentos**: Se almacenan los archivos en el directorio `data/`.  
2. **Ejecución de Grobid**: Se utiliza la API de Grobid para convertir los PDFs en XMLs estructurados.  
3. **Extracción de información clave**: Se extraen abstracts, figuras y enlaces a partir de los archivos XML generados.  
4. **Visualización de datos**: Se generan una nube de palabras clave y un gráfico de figuras por artículo.  

El pipeline fue implementado en Python, utilizando `requests` para interactuar con la API de Grobid y `xml.etree.ElementTree` para parsear los archivos XML.  

---

### **2.2. Extracción de Información**  

#### **2.2.1. Nube de Palabras Clave**  
**Enfoque:**  
- Se extraen los **abstracts** de los archivos XML generados.  
- Se combinan en un solo texto y se eliminan caracteres especiales.  
- Se genera una **nube de palabras** con `wordcloud.WordCloud`.  

**Validación:**  
- Se revisó manualmente que los abstracts extraídos desde el XML correspondieran a los textos en los artículos originales.  
- Se verificó que las palabras clave reflejaran términos frecuentes en los abstracts procesados.  
- Se generaron diferentes versiones de la nube de palabras para confirmar que el resultado era consistente.  

---

#### **2.2.2. Conteo de Figuras por Artículo**  
**Enfoque:**  
- Se buscan etiquetas `<tei:figure>` dentro del XML de cada artículo.  
- Se cuenta la cantidad de apariciones de esta etiqueta en cada archivo.  
- Se genera un gráfico de barras con `matplotlib.pyplot`.  

**Validación:**  
- Se realizó una **comparación manual** entre el número de figuras reportado y el número de imágenes visibles en los PDFs originales.  
- Se ajustó el código para asegurar que solo se contaran las figuras correctamente etiquetadas.  
- Se generaron gráficos en diferentes formatos para confirmar la consistencia de los resultados.  

---

#### **2.2.3. Extracción de Enlaces Externos**  
**Enfoque:**  
- Se buscan etiquetas `<tei:ref>` en los XMLs.  
- Se extraen los valores del atributo `target`, descartando los enlaces internos.  
- Se almacenan en un archivo JSON (`links_per_paper.json`).  

**Validación:**  
- Se realizó una **verificación manual** de los enlaces extraídos comparándolos con los que aparecen en los PDFs.  
- Se descartaron referencias que no correspondían a URLs externas.  
- Se utilizó una prueba con un PDF de ejemplo para asegurar que la extracción funcionaba correctamente.  

---

## **3. Pruebas y Validación**  

Para validar la precisión del pipeline, se implementaron pruebas unitarias y validaciones manuales:  

### **3.1. Pruebas Unitarias (Archivo `test.py`)**  
Se desarrollaron pruebas automatizadas utilizando `pytest` para verificar la funcionalidad de los scripts:  
- **Prueba de procesamiento de PDFs**: Verifica que los XMLs se generen correctamente.  
- **Prueba de extracción de abstracts**: Confirma que los abstracts se extraen correctamente de los XMLs.  
- **Prueba de conteo de figuras**: Asegura que se detecten correctamente las figuras en cada artículo.  
- **Prueba de extracción de enlaces**: Valida que se extraigan URLs válidas de los XMLs.  
- **Prueba de generación de la nube de palabras**: Comprueba que el archivo `wordcloud.png` se genera correctamente.  
- **Prueba de generación del gráfico de figuras**: Confirma que `figures_per_paper.png` se genera correctamente.  

### **3.2. Validación Manual**  
Además de las pruebas automatizadas, se realizó una **validación manual** de los resultados:  
- **Comparación visual de los abstracts extraídos con los textos originales** en los PDFs.  
- **Verificación manual del conteo de figuras**, asegurando que coincidiera con las imágenes en los artículos.  
- **Revisión de los enlaces extraídos** en comparación con los documentos originales.  

---

## **4. Reproducibilidad del Experimento**  

Se documentó detalladamente el entorno y las dependencias necesarias para ejecutar el pipeline de manera reproducible.  

### **4.1. Configuración del Entorno**  
Se creó un archivo **`requirements.txt`** con todas las dependencias necesarias para ejecutar el pipeline.  

### **4.2. Dockerización**  
Se desarrolló un **Dockerfile** y un archivo **docker-compose.yml** para contenerizar la aplicación y garantizar su correcta ejecución en cualquier entorno.  

---

## **5. Posibles Mejoras y Limitaciones**
### **5.1. Posibles Mejoras**

- Implementar una mejor filtración de palabras clave para mejorar la nube de palabras.
- Utilizar procesamiento de lenguaje natural (NLP) para identificar términos más relevantes en los abstracts.
- Aplicar reconocimiento de imágenes para analizar el contenido de las figuras en los artículos.
- Optimizar la extracción de enlaces, filtrando solo aquellos de interés para el análisis.

### **5.2. Limitaciones**

- La calidad de la extracción de datos depende de la estructura del XML generado por Grobid.
- Grobid puede no reconocer correctamente todos los elementos en algunos artículos, lo que puede afectar los resultados.
- La validación manual fue limitada a una muestra, por lo que podrían existir errores en algunos artículos.