"""This is the script responsible for running our code."""

# Fast API imports for web server and post requests
from typing import List
from fastapi import FastAPI
from fastapi import UploadFile
import uvicorn

from parse_document import upload_documents_and_generate_response
from helpers import save_response
from llama_calculator import solve_math_problem


app = FastAPI()

@app.get("/")
def read_root():
    """Root function."""
    return {"message": "Hello, this is the root!"}

@app.post("/upload_documents_and_generate_reponse")
def create_response(user_query: str, pdf_files: List[UploadFile]):
    """This function uploads files provided by the user, accepts a user-specified query,
      and returns a response based on the user's query."""

    # Upload documents and generate a response from OpenAI
    response = upload_documents_and_generate_response(pdf_files, user_query)

    # Save the response to a text file locally.
    save_response(user_query, response)

    return {"response": response}

@app.post("/calculator")
def calculator(question: str):
    """This function acts as a calculator, it takes a math
        problem as input and returns the answer."""

    answer = solve_math_problem(question)

    return {"answer": answer}

# This is the main entry point for the FastAPI application.
if __name__ == "__main__":

    # Run the FastAPI app with Uvicorn server - navigate to http://localhost:5001/docs
    uvicorn.run("main:app", host="0.0.0.0", port=5001, log_level="info", reload=True)
