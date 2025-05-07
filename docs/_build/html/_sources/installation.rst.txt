=============================================
Instalación y Configuración
=============================================

Existen dos métodos para ejecutar la aplicación:  

1️⃣ **Usando Docker Compose (Recomendado)** – Corre Grobid y la aplicación en contenedores automáticamente.  
2️⃣ **Usando Python 3.10+ y un entorno virtual** – Ejecuta la aplicación sin Docker, pero usa **Grobid en un contenedor Docker**.

Ambos métodos permiten procesar los artículos y generar las visualizaciones automáticamente.

-------------------------------------------------------------

1️⃣ **Método 1: Usando Docker Compose (Recomendado)**
-------------------------------------------------------------

Este método inicia **Grobid y la aplicación** en contenedores separados, lo que facilita la ejecución sin instalar dependencias manualmente.

**Paso 1: Clonar el repositorio**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: bash

   git clone https://github.com/SergonM/ArticlesAnalysisGrobid.git
   cd ArticlesAnalysisGrobid

**Paso 2: Agregar los artículos en la carpeta `data/`**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- En la carpeta `data/` hay **2 artículos en PDF** por defecto.
- Puedes reemplazarlos o agregar nuevos documentos en esta carpeta.

**Paso 3: Iniciar los servicios con Docker Compose**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Ejecuta el siguiente comando para levantar los servicios (en versiones de Docker antiguas es docker-compose):

.. code-block:: bash

   docker compose up -d

🔹 Esto iniciará:  
- **Grobid** en `http://localhost:8070`  
- **La aplicación**, que interactúa con Grobid y procesa los artículos  

📌 **Notas**:
- Si Grobid no responde, verifica que el servicio esté activo en `http://localhost:8070/api/isalive`.
- Para detener los servicios:

.. code-block:: bash

   docker compose down

-------------------------------------------------------------

2️⃣ **Método 2: Usando Python 3.10+ con Virtualenv y Docker para Grobid**
-------------------------------------------------------------------------

Este método usa **Python 3.10+** para ejecutar la aplicación y un contenedor **Docker para Grobid**.

**Paso 1: Clonar el repositorio**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: bash

   git clone https://github.com/SergonM/ArticlesAnalysisGrobid.git
   cd ArticlesAnalysisGrobid

**Paso 2: Crear y activar un entorno virtual**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Ejecuta los siguientes comandos para crear un entorno virtual en Python:

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate  # En Linux/macOS
   venv\Scripts\activate     # En Windows

**Paso 3: Instalar las dependencias**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: bash

   pip install -r requirements.txt

**Paso 4: Agregar los artículos en la carpeta `data/`**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- En la carpeta `data/` hay **2 artículos en PDF** por defecto.
- Puedes reemplazarlos o agregar nuevos documentos en esta carpeta.

**Paso 5: Iniciar Grobid con Docker**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Ejecuta el siguiente comando para iniciar **Grobid** en un contenedor **Docker**:

.. code-block:: bash

   docker run -t --rm -p 8070:8070 -e JAVA_TOOL_OPTIONS=-XX:-UseContainerSupport lfoppiano/grobid:0.8.1

🔹 Esto iniciará **Grobid en `http://localhost:8070`**.
🔹 Deja esta terminal abierta mientras se ejecuta Grobid.

**Paso 6: Ejecutar la aplicación manualmente**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
En otra terminal, asegúrate de que el entorno virtual sigue activado y ejecuta:

.. code-block:: bash

   python src/main.py

📌 **Notas**:
- Grobid debe estar corriendo antes de ejecutar la aplicación.
- Si Grobid deja de responder, reinicia el contenedor con el **Paso 5**.

-------------------------------------------------------------

Ambos métodos permiten procesar los artículos y generar las visualizaciones automáticamente. 🚀
