import os
import sys

# Agregar `src/` al path de Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


import pytest
import shutil
import json
from config import OUTPUT_DIR, DATA_DIR
from extraction import extract_abstracts, count_figures, extract_links
from process import process_all_pdfs, process_pdf
from visualization import generate_wordcloud, plot_figures
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas



@pytest.fixture(autouse=True)
def clear_output_dir():
    """Limpia la carpeta de salida antes de cada prueba."""
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)  # Elimina la carpeta y todo su contenido
    os.makedirs(OUTPUT_DIR, exist_ok=True)  # La vuelve a crear vacía

    # 2. Crear un mini PDF con un link y un abstract
    pdf_path = os.path.join(DATA_DIR, "test_document.pdf")
    create_mini_pdf(pdf_path)
    

def create_mini_pdf(pdf_path):
    """Crea un mini PDF con un enlace y un abstract de prueba."""
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.setFont("Helvetica", 12)

    # Escribir el título
    c.drawString(100, 750, "Mini Documento de Prueba")

    # Escribir el abstract
    abstract_text = "Este es un pequeño abstract de prueba generado automáticamente para pruebas."
    c.drawString(100, 720, "Abstract:")
    c.drawString(100, 700, abstract_text)

    # Escribir un enlace
    link_text = "Más información aquí:"
    c.drawString(100, 670, link_text)
    c.setFillColorRGB(0, 0, 1)  # Azul
    c.drawString(200, 670, "https://example.com")
    c.linkURL("https://example.com", (200, 660, 400, 680))

    # Guardar el PDF
    c.save()


def test_process_pdf():
    """Prueba el procesamiento del mini PDF en DATA_DIR."""
    pdf_path = os.path.join(DATA_DIR, "test_document.pdf")
    process_pdf(pdf_path)

    # Verificar que se haya generado un XML
    xml_files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(".xml")]
    assert len(xml_files) > 0, "No se generaron archivos XML tras el procesamiento"

def test_extract_abstracts():
    """Prueba la extracción del abstract desde el XML generado."""
    process_pdf(os.path.join(DATA_DIR, "test_document.pdf"))
    abstracts = extract_abstracts()

    assert isinstance(abstracts, list), "El resultado no es una lista"
    assert len(abstracts) > 0, "No se extrajo ningún abstract"
    assert isinstance(abstracts[0], str), "Los abstracts deben ser cadenas de texto"

def test_count_figures():
    """Prueba el conteo de figuras en el mini PDF procesado."""
    process_pdf(os.path.join(DATA_DIR, "test_document.pdf"))
    figure_counts = count_figures()

    assert isinstance(figure_counts, dict), "El resultado debe ser un diccionario"
    assert len(figure_counts) > 0, "No se encontraron figuras"
    assert isinstance(list(figure_counts.values())[0], int), "El conteo de figuras debe ser un número entero"

def test_extract_links():
    """Prueba la extracción del enlace desde el XML generado."""
    process_pdf(os.path.join(DATA_DIR, "test_document.pdf"))
    extract_links()

    output_file = os.path.join(OUTPUT_DIR, "links_per_paper.json")
    assert os.path.exists(output_file), "El archivo JSON de enlaces no fue generado"

    with open(output_file, "r", encoding="utf-8") as f:
        links_data = json.load(f)

    assert isinstance(links_data, dict), "El resultado debe ser un diccionario"
    assert len(links_data) > 0, "No se extrajo ningún enlace"

def test_generate_wordcloud():
    """Prueba la generación de una nube de palabras con el mini PDF."""
    process_pdf(os.path.join(DATA_DIR, "test_document.pdf"))
    generate_wordcloud()

    wordcloud_file = os.path.join(OUTPUT_DIR, "wordcloud.png")
    assert os.path.exists(wordcloud_file), "El archivo de la nube de palabras no fue generado"

def test_plot_figures():
    """Prueba la generación del gráfico de figuras basado en el mini PDF."""
    process_pdf(os.path.join(DATA_DIR, "test_document.pdf"))
    plot_figures()

    figures_file = os.path.join(OUTPUT_DIR, "figures_per_paper.png")
    assert os.path.exists(figures_file), "El archivo del gráfico de figuras no fue generado"
