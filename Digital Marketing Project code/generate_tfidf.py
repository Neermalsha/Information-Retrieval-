import os
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# Load text files
text_files_path = "output_texts"
documents = []

for filename in os.listdir(text_files_path):
    if filename.endswith('.txt'):
        with open(os.path.join(text_files_path, filename), 'r', encoding='utf-8') as f:
            documents.append(f.read())

# Generate TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Save the outputs
with open('tfidf_vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
with open('tfidf_matrix.pkl', 'wb') as f:
    pickle.dump(tfidf_matrix, f)
with open('doc_names.pkl', 'wb') as f:
    pickle.dump([filename for filename in os.listdir(text_files_path) if filename.endswith('.txt')], f)

print("TF-IDF generated and saved.")
