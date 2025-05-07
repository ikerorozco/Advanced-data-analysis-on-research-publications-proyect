import os
import xml.etree.ElementTree as ET
import json
from config import NAMESPACE, OUTPUT_DIR

def extract_abstracts():
    """Extrae los abstracts de los archivos XML procesados."""
    abstracts = []
    for file in os.listdir(OUTPUT_DIR):
        if file.endswith(".xml"):
            tree = ET.parse(os.path.join(OUTPUT_DIR, file))
            root = tree.getroot()
            for abstract in root.findall(".//tei:abstract//tei:p", NAMESPACE):
                if abstract.text:
                    abstracts.append(abstract.text.strip())
    return abstracts