"""This script parses a document using the LlamaParse class from the llama_cloud_services module."""

# bring in package dependencies
import os
import dspy
from dotenv import load_dotenv
from llama_cloud_services import LlamaParse
from llama_index.core import SimpleDirectoryReader

from helpers import save_parsed_document, clean_directory, save_uploaded_files

# Bring in our env vars
load_dotenv("keys.env")

# Where the uploaded documents are stored.
DOCS_PATH = "data"


def upload_documents_and_generate_response(pdf_files, user_query):
    """This function uploads files provided by the user, accepts a user-specified query"""

    # Remove any existing files in the DOCS_PATH directory from the last run.
    clean_directory(DOCS_PATH)

    # Set up parser
    parser = LlamaParse(
        result_type="markdown"  # "markdown" and "text" are available
    )

    # Save each file object to the local directory for now
    save_uploaded_files(pdf_files)

    # Use SimpleDirectoryReader to parse our file(s)
    file_extractor = {".pdf": parser}
    documents = SimpleDirectoryReader(input_dir=DOCS_PATH,
                                    file_extractor=file_extractor).load_data()

    save_parsed_document(documents)

    # Load gpt-40-mini model from OpenAI using the DSPy framework
    lm = dspy.LM('openai/gpt-4o-mini', api_key=os.getenv("OPENAI_API_KEY"))
    dspy.configure(lm=lm)

    # Set up the guardrails for the model to follow when generating a response
    rag = dspy.ChainOfThought('context, question -> response')

    response = rag(context=documents, question=user_query)

    return response
