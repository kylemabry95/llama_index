## Small-Scale RAG project using LlamaIndex and OpenAI

- This is a proof of concept project for analyzing PDF documents using OpenAI and Llamaindex. 
The application takes PDF file(s) and a user-specified prompt as input and returns an AI generated 
response to the prompt that includes relevant information from the uploaded PDF documents. This is a basic
demonstration of the RAG concept. 

## Quick Start

- Create a `./data` folder where your PDF document(s) are located and enter the file
  path into the `DOCS_PATH` variable within the parse_document.py script.

- Create a `keys.env` file in the project directory for your API keys and use the following 
names: `LLAMA_CLOUD_API_KEY` and `OPENAI_API_KEY`

- To install dependencies and run the script enter the two following commands in the terminal:
`pip install -r requirements.txt`

- From the terminal, run the following command to activate the fastAPI server hosted by uvicorn: `python3 src/main.py`

- In a web-browser of your choice navigate to `http://localhost:5001/docs` and upload your PDF files + enter the
prompt for the AI to solve.

- When you're ready to integrate the application into a Kubernetes cluster, run the following code in the terminal 
(with Docker running in the background) to build a portable Docker image: `docker build .`
