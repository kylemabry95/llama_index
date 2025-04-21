## Small-Scale RAG project using LlamaIndex and OpenAI

- This is a proof of concept project for analyzing PDF documents using OpenAI and Llamaindex. 

## Quick Start

- Create a `./data` folder where your PDF document(s) are located and enter the file
  path into the `DOCS_PATH` variable within the parse_document.py script.

- Update the `USER_QUERY` variable to reflect the question you'd like to ask pertaining
  to the PDF document(s).

- Create a `keys.env` file in the project directory for your API keys and use the following 
names: `LLAMA_CLOUD_API_KEY` and `OPENAI_API_KEY`

- To install dependencies and run the script enter the two following commands in the terminal:
`pip install -r requirements.txt` followed by `python3 parse_document.py`

- In from terminal run the following command to activate the fastAPI server hosted by uvicorn: `python3 main.py`

- When you're ready to integrate the application into a Kubernetes cluster, run the following code in the terminal 
(with Docker running in the background) `docker build .`
