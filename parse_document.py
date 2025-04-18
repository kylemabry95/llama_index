"""This script parses a document using the LlamaParse class from the llama_cloud_services module."""
# bring in our LLAMA_CLOUD_API_KEY
from dotenv import load_dotenv

# bring in deps
from llama_cloud_services import LlamaParse
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

# Edit the document location path to point to your files
DOCS_PATH = "data"
# Edit the prompt that's being used to analyze the document
USER_QUERY = "Summarize Kyle Mabry's resume and determine if he is a good fit for a senior data scientist position"

# bring in our env vars
load_dotenv("keys.env")

# set up parser
parser = LlamaParse(
    result_type="markdown"  # "markdown" and "text" are available
)

# use SimpleDirectoryReader to parse our file
file_extractor = {".pdf": parser}
documents = SimpleDirectoryReader(input_dir=DOCS_PATH,
                                   file_extractor=file_extractor).load_data()

# Save the parsed document to a text file
with open("parsed_documents.txt", "a", encoding="utf-8") as f:
    for doc in documents:
        f.write(doc.text)
        f.write("\n\n")  # Add a newline between documents


# create an index from the parsed markdown
index = VectorStoreIndex.from_documents(documents)

# create a query engine for the index
query_engine = index.as_query_engine()

# query the engine
response = query_engine.query(USER_QUERY)
print(response)
