"""This contains helper functions so that the rest of our code is clean"""

import os

def clean_directory(DOCS_PATH):
    """This function removes all files in the DOCS_PATH directory."""
    for filename in os.listdir(DOCS_PATH):
        file_path = os.path.join(DOCS_PATH, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Error removing file {file_path}: {e}")

def save_uploaded_files(pdf_files):
    """This function saves the uploaded files to the local directory."""
    for file in pdf_files:
        file_path = os.path.join("data", file.filename)
        with open(file_path, "wb") as buffer:
            file_content = file.file.read()
            buffer.write(file_content)

def save_parsed_document(documents):
    """Save the parsed document to a text file."""
    with open("parsed_documents.txt", "a", encoding="utf-8") as f:
        for doc in documents:
            f.write(doc.text)
            f.write("\n\n")  # Add a newline between documents

def save_response(user_query, response):
    """This function saves the response to a text file locally."""
    with open("generated_responses.txt", "a", encoding="utf-8") as f:
        f.write("User query: " + user_query + "\n\n")
        f.write("User response: " + response.get("response", ""))
        f.write("\n\n\n New Response \n\n\n")