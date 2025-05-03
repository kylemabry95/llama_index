"""Code for a calculator using DSPy."""
import os
import dspy
from dotenv import load_dotenv

from helpers import clean_directory

# Where the uploaded documents are stored.
DOCS_PATH = "data"

# Bring in our env vars
load_dotenv("keys.env")

def solve_math_problem(user_question):
    """This function acts as a calculator, it takes a math 
        problem as input and returns the answer as a float."""

    # Clean the DOCS_PATH directory
    clean_directory(DOCS_PATH)

    # Configure the LLM
    lm = dspy.LM('openai/o1-mini', api_key = os.getenv("OPENAI_API_KEY"),
                                        temperature=1.0, max_tokens=20000)
    dspy.configure(lm=lm)

    # Create a chain of thought template for the calculator
    math = dspy.ChainOfThought("question -> answer: float")

    # Call the Chain of Thought with the question
    result = math(question=user_question)

    return result
