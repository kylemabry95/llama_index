"""This script parses a document using the LlamaParse class from the llama_cloud_services module."""

# bring in package dependencies
import os
from dotenv import load_dotenv
from llama_cloud_services import LlamaParse
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

# Bring in our env vars
load_dotenv("keys.env")

# Where the uploaded documents are stored.
DOCS_PATH = "data"


def upload_documents_and_generate_response(pdf_files, user_query):
    """This function uploads files provided by the user, accepts a user-specified query"""

    # Remove any existing files in the DOCS_PATH directory from the last run.
    for filename in os.listdir(DOCS_PATH):
        file_path = os.path.join(DOCS_PATH, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Error removing file {file_path}: {e}")

    # Set up parser
    parser = LlamaParse(
        result_type="markdown"  # "markdown" and "text" are available
    )

    # Save each file object to the local directory for now
    # TODO: Save hard copies of the files to a cloud provider to save local storage.
    for file in pdf_files:
        file_path = os.path.join(DOCS_PATH, file.filename)
        with open(file_path, "wb") as buffer:
            file_content = file.file.read()
            buffer.write(file_content)

    # Use SimpleDirectoryReader to parse our file(s)
    file_extractor = {".pdf": parser}
    documents = SimpleDirectoryReader(input_dir=DOCS_PATH,
                                    file_extractor=file_extractor).load_data()

    # Save the parsed document to a text file
    with open("parsed_documents.txt", "a", encoding="utf-8") as f:
        for doc in documents:
            f.write(doc.text)
            f.write("\n\n")  # Add a newline between documents


    # Create an index from the parsed markdown
    index = VectorStoreIndex.from_documents(documents)

    # Create a query engine for the index
    query_engine = index.as_query_engine()

    # Query the engine
    response = query_engine.query(user_query)

    # Return the response for debugging
    print(response)

    return response
