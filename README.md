# LlamaIndex Multi-Tool RAG Application

A comprehensive Retrieval-Augmented Generation (RAG) application built with LlamaIndex, DSPy, and FastAPI that provides document analysis, mathematical calculations, and Wikipedia search capabilities.

## Features

- **📄 PDF Document Analysis**: Upload and analyze PDF documents using LlamaParse and OpenAI GPT models
- **🧮 AI Calculator**: Solve complex mathematical problems using OpenAI's o1-mini model
- **🔍 Wikipedia Search**: Intelligent Wikipedia search with ReAct framework integration
- **🚀 FastAPI Web Interface**: Interactive API with automatic documentation
- **🐳 Docker Support**: Containerized deployment for easy scaling
- **☁️ Cloud Integration**: Built-in support for LlamaCloud services

## Architecture

The application consists of several modular components:

- **FastAPI Server** (`main.py`): RESTful API endpoints with automatic documentation
- **Document Parser** (`parse_document.py`): PDF processing using LlamaParse and LlamaIndex
- **Calculator Module** (`llama_calculator.py`): Mathematical problem solving with DSPy
- **Wikipedia RAG** (`wikipedia_rag_model.py`): Wikipedia search with ReAct reasoning
- **Helper Functions** (`helpers.py`): Utility functions for file management and response handling

## Prerequisites

- Python 3.11+
- OpenAI API key
- LlamaCloud API key
- Docker (optional, for containerized deployment)

## Quick Start

### 1. Environment Setup

Create a `keys.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
LLAMA_CLOUD_API_KEY=your_llama_cloud_api_key_here
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create Data Directory

```bash
mkdir data
```

### 4. Run the Application

```bash
python src/main.py
```

The FastAPI server will start on `http://localhost:5001`

### 5. Access the API Documentation

Navigate to `http://localhost:5001/docs` in your web browser to access the interactive API documentation powered by Swagger UI.

## API Endpoints

### Document Analysis
**POST** `/upload_documents_and_generate_reponse`
- Upload PDF files and get AI-generated responses based on document content
- **Parameters**: 
  - `user_query` (string): Your question about the documents
  - `pdf_files` (array): PDF files to analyze

### Calculator
**POST** `/calculator`
- Solve mathematical problems using AI
- **Parameters**:
  - `question` (string): Mathematical problem to solve
- **Returns**: Numerical answer with reasoning

### Wikipedia Search
**POST** `/search_wikipedia`
- Search Wikipedia and get AI-enhanced responses
- **Parameters**:
  - `query` (string): Search term or question
- **Returns**: Comprehensive answer based on Wikipedia content

## Usage Examples

### Document Analysis
```python
import requests

# Upload PDFs and ask questions
files = [('pdf_files', open('document.pdf', 'rb'))]
data = {'user_query': 'What are the key findings in this research?'}
response = requests.post('http://localhost:5001/upload_documents_and_generate_reponse', 
                        files=files, data=data)
```

### Calculator
```python
import requests

response = requests.post('http://localhost:5001/calculator', 
                        json={'question': 'What is the derivative of x^2 + 3x + 2?'})
```

### Wikipedia Search
```python
import requests

response = requests.post('http://localhost:5001/search_wikipedia', 
                        json={'query': 'Explain quantum computing principles'})
```

## Docker Deployment

### Build the Docker Image
```bash
docker build -t llama-rag-app .
```

### Run the Container
```bash
docker run -p 5001:5001 --env-file keys.env llama-rag-app
```

### Kubernetes Deployment
The application is designed to be Kubernetes-ready. After building the Docker image, you can deploy it to your Kubernetes cluster using standard Kubernetes manifests.

## Project Structure

```
├── src/
│   ├── main.py                    # FastAPI application entry point
│   ├── parse_document.py          # PDF parsing and analysis
│   ├── llama_calculator.py        # Mathematical problem solver
│   ├── wikipedia_rag_model.py     # Wikipedia search functionality
│   └── helpers.py                 # Utility functions
├── data/                          # Directory for uploaded documents
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Container configuration
├── keys.env                       # Environment variables (create this)
└── README.md                      # Project documentation
```

## Technical Stack

- **Framework**: FastAPI for REST API
- **AI/ML**: 
  - OpenAI GPT-4o-mini for general tasks
  - OpenAI o1-mini for mathematical reasoning
  - DSPy for structured AI programming
- **Document Processing**: LlamaParse, LlamaIndex
- **Search**: ColBERTv2 for Wikipedia retrieval
- **Server**: Uvicorn ASGI server
- **Containerization**: Docker

## Configuration

### Model Settings
- **Document Analysis**: Uses GPT-4o-mini with Chain of Thought reasoning
- **Calculator**: Uses o1-mini with enhanced mathematical capabilities
- **Wikipedia Search**: Combines ColBERTv2 retrieval with GPT-4o-mini reasoning

### File Management
- Uploaded files are temporarily stored in the `data/` directory
- Parsed documents and responses are saved locally for reference
- Automatic cleanup prevents storage bloat

## Development

### Adding New Endpoints
1. Define new endpoint in `main.py`
2. Create corresponding function in appropriate module
3. Update helper functions if needed
4. Test using the FastAPI documentation interface

### Extending Functionality
The modular architecture makes it easy to add new features:
- Add new AI models by updating the DSPy configuration
- Integrate additional document types by extending the parser
- Add new data sources by creating new retrieval modules

## Troubleshooting

### Common Issues
- **API Key Errors**: Ensure your `keys.env` file is properly configured
- **Port Conflicts**: Change the port in `main.py` if 5001 is occupied
- **Memory Issues**: Large PDFs may require increased system memory
- **Docker Issues**: Ensure Docker is running and ports are available

### Logs and Debugging
- Check console output for detailed error messages
- Response logs are saved to `generated_responses.txt`
- Parsed documents are saved to `parsed_documents.txt`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly using the API documentation
5. Submit a pull request

## License

This project is open source and available under standard licensing terms.

## Support

For issues and questions:
- Check the GitHub Issues page
- Review the API documentation at `/docs`
- Ensure all environment variables are properly configured

---

**Note**: This is a proof-of-concept application demonstrating RAG capabilities. For production use, consider implementing additional security measures, error handling, and scalability optimizations.
