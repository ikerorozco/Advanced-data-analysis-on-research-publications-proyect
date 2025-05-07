import os
import requests
import time
import numpy as np
from config import GROBID_URL, HEADERS, DATA_DIR, OUTPUT_DIR
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity

def process_pdf(file_path):
    """Envía un PDF a Grobid y guarda la respuesta XML."""
    with open(file_path, "rb") as pdf_file:
        response = requests.post(GROBID_URL, files={"input": pdf_file}, headers=HEADERS)
    
    if response.status_code == 200:
        output_file = os.path.join(OUTPUT_DIR, os.path.basename(file_path).replace(".pdf", ".xml"))
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"Procesado: {file_path} -> {output_file}")
    else:
        print(f"Error procesando {file_path}: {response.status_code}")

def process_all_pdfs():
    """Procesa todos los PDFs en el directorio DATA_DIR."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    pdf_files = [f for f in os.listdir(DATA_DIR) if f.endswith(".pdf")]
    
    for pdf in pdf_files:
        process_pdf(os.path.join(DATA_DIR, pdf))
        time.sleep(2)  # Evitar sobrecargar Grobid

def cluster_abstracts(abstracts, n_clusters=5):
    """
    Clusters abstracts using sentence transformers and KMeans.
    
    Args:
        abstracts (list): List of abstract texts
        n_clusters (int): Number of clusters to create
        
    Returns:
        tuple: (cluster_labels, embeddings, similarity_matrix)
    """
    # Load the sentence transformer model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Generate embeddings for all abstracts
    embeddings = model.encode(abstracts)
    
    # Perform clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(embeddings)
    
    # Calculate similarity matrix
    similarity_matrix = cosine_similarity(embeddings)
    
    return cluster_labels, embeddings, similarity_matrix

def get_similar_abstracts(abstracts, target_index, similarity_matrix, top_n=5):
    """
    Get the most similar abstracts to a target abstract.
    
    Args:
        abstracts (list): List of abstract texts
        target_index (int): Index of the target abstract
        similarity_matrix (numpy.ndarray): Matrix of cosine similarities
        top_n (int): Number of similar abstracts to return
        
    Returns:
        list: List of tuples (index, similarity_score, abstract_text)
    """
    # Get similarity scores for the target abstract
    similarities = similarity_matrix[target_index]
    
    # Get indices of top N similar abstracts (excluding the target itself)
    similar_indices = np.argsort(similarities)[::-1][1:top_n+1]
    
    # Create list of results
    results = [(idx, similarities[idx], abstracts[idx]) for idx in similar_indices]
    
    return results
