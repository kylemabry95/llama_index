"""This script searchs Wikipedia for a given query and returns responses based
on the information on the page."""

import os
import dspy
from helpers import clean_directory

# Where the uploaded documents are stored.
DOCS_PATH = "data"

def search_wikipedia(query: str):
    """This function searches Wikipedia for a given query and returns the top 3 results."""
    results = dspy.ColBERTv2(url='http://20.102.90.50:2024/wiki17_abstracts')(query, k=3)
    return [x['text'] for x in results]


def search_wikipedia_react(query: str):
    """This function searches Wikipedia for a given query and returns the top 3 results."""

    # Remove any existing files in the DOCS_PATH directory from the last run.
    clean_directory(DOCS_PATH)

    lm = dspy.LM('openai/gpt-4o-mini', api_key = os.getenv("OPENAI_API_KEY"))
    dspy.configure(lm=lm)

    react = dspy.ReAct("question -> answer: str", tools=[search_wikipedia])

    pred = react(question=query)
    return pred.answer
