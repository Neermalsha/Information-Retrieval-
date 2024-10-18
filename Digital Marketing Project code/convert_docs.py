import os
from docx import Document

# Set your documents folder
documents_folder = r"C:\Users\nirma\Information R\Document"
text_output_path = "output_texts"  # Folder to save converted text files

if not os.path.exists(text_output_path):
    os.makedirs(text_output_path)

# Convert each .docx file to text
for filename in os.listdir(documents_folder):
    if filename.endswith('.docx'):
        doc = Document(os.path.join(documents_folder, filename))
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        with open(os.path.join(text_output_path, f"{filename}.txt"), 'w', encoding='utf-8') as text_file:
            text_file.write('\n'.join(full_text))

print("Documents converted to text format.")


