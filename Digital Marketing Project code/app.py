from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import numpy as np

app = Flask(__name__)

# Load documents (make sure to replace this with your digital marketing docs)
documents = [
    "Digital marketing strategies in 2024.pdf",
    "SEO optimization techniques.pdf",
    "Content marketing and engagement.pdf",
    "The role of social media in digital marketing.pdf",
    # Add more document names here
]

# Placeholder for document content (assuming they are cleaned text, not raw PDFs)
document_content = [
    "Text content of Digital marketing strategies in 2024.",
    "Text content of SEO optimization techniques.",
    "Text content of Content marketing and engagement.",
    "Text content of The role of social media in digital marketing.",
    # Add text content for all documents here
]

# Initialize TF-IDF vectorizer
vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(document_content)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    query_vector = vectorizer.transform([query])

    # Compute cosine similarity
    similarity_scores = cosine_similarity(query_vector, doc_vectors).flatten()
    
    # Get top 5 most similar documents
    top_indices = similarity_scores.argsort()[-5:][::-1]
    results = [(documents[i], similarity_scores[i]) for i in top_indices]

    return render_template('result.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)

