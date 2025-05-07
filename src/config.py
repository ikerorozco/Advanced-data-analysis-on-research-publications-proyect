import os

# Rutas de archivos
DATA_DIR = "data/"  #: str: Directorio donde se almacenan los datos.
OUTPUT_DIR = "output/"  #: str: Directorio donde se guardan los archivos de salida.
GROBID_DIR = "grobid-0.8.1/"  #: str: Directorio donde está instalado Grobid.

# Configuración de Grobid
GROBID_URL = os.getenv("GROBID_URL", "http://localhost:8070/api/processFulltextDocument")
"""str: URL del servicio Grobid para el procesamiento de documentos."""

GROBID_ALIVE = os.getenv("GROBID_ALIVE", "http://localhost:8070/api/isalive")
"""str: URL para verificar si Grobid está activo."""

HEADERS = {"Accept": "application/xml"}
"""dict: Cabeceras HTTP utilizadas para las peticiones a Grobid."""

# Namespace para XML TEI
NAMESPACE = {'tei': 'http://www.tei-c.org/ns/1.0'}
"""dict: Namespace utilizado en los archivos XML TEI."""
