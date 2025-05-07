import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re
from extraction import extract_abstracts, count_figures
from config import OUTPUT_DIR

def generate_wordcloud():
    """Genera una nube de palabras basada en los abstracts."""
    abstracts = extract_abstracts()
    text = " ".join(abstracts)
    text = re.sub(r'[^a-zA-Z ]', '', text)  # Filtra caracteres no alfabéticos
    
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(os.path.join(OUTPUT_DIR, "wordcloud.png"))
    print("Nube de palabras generada: output/wordcloud.png")
