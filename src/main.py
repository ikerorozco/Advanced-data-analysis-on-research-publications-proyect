import time
import requests
from process import process_all_pdfs, cluster_abstracts, get_similar_abstracts
from extraction import extract_links, extract_abstracts
from visualization import generate_wordcloud, plot_figures
from config import GROBID_URL, GROBID_ALIVE

def check_grobid_alive():
    """Verifica si el servicio Grobid está activo antes de ejecutar cualquier tarea."""
    print("Verificando si Grobid está activo...")
    while True:
        try:
            response = requests.get(GROBID_ALIVE)
            if response.status_code == 200:
                print("Grobid está activo. Continuando con el proceso...")
                break
            else:
                print("Grobid no está disponible. Esperando...")
        except requests.exceptions.RequestException:
            print(GROBID_ALIVE)
            print("No se pudo conectar con Grobid. Reintentando en 5 segundos...")
        time.sleep(5)

def analyze_abstracts():
    """Analiza los abstracts usando clustering y similitud."""
    print("\nExtrayendo abstracts...")
    abstracts = extract_abstracts()
    
    if not abstracts:
        print("No se encontraron abstracts para analizar.")
        return
    
    print(f"\nSe encontraron {len(abstracts)} abstracts.")
    
    # Realizar clustering
    print("\nRealizando clustering de abstracts...")
    cluster_labels, embeddings, similarity_matrix = cluster_abstracts(abstracts, n_clusters=5)
    
    # Mostrar distribución de clusters
    unique_labels = set(cluster_labels)
    print("\nDistribución de clusters:")
    for label in unique_labels:
        count = list(cluster_labels).count(label)
        print(f"Cluster {label}: {count} abstracts")
    
    # Mostrar ejemplos de abstracts similares
    print("\nEjemplos de abstracts similares:")
    for i in range(min(3, len(abstracts))):  # Mostrar para los primeros 3 abstracts
        print(f"\nAbstract original {i+1}:")
        print(abstracts[i][:200] + "..." if len(abstracts[i]) > 200 else abstracts[i])
        
        similar = get_similar_abstracts(abstracts, i, similarity_matrix, top_n=2)
        print("\nAbstracts similares:")
        for idx, score, text in similar:
            print(f"\nSimilitud: {score:.4f}")
            print(text[:200] + "..." if len(text) > 200 else text)

def main_menu():
    """Menú principal para ejecutar opciones del pipeline."""
    while True:
        print("\nSeleccione una opción:")
        print("1. Procesar PDFs con Grobid")
        print("2. Generar visualizaciones")
        print("3. Extraer enlaces")
        print("4. Analizar similitud de abstracts")
        print("5. Salir")
        
        choice = input("Ingrese su elección: ")
        
        if choice == "1":
            process_all_pdfs()
        elif choice == "2":
            generate_wordcloud()
            plot_figures()
        elif choice == "3":
            extract_links()
        elif choice == "4":
            analyze_abstracts()
        elif choice == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    check_grobid_alive()
    #main_menu()
    process_all_pdfs()
    generate_wordcloud()
    analyze_abstracts()
    print("Saliendo del programa.")
