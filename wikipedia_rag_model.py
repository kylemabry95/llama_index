"""This script searchs Wikipedia for a given query and returns responses based
on the information on the page."""

import dspy
from dotenv import load_dotenv
import os


def search_wikipedia(query: str):
    """This function searches Wikipedia for a given query and returns the top 3 results."""
    results = dspy.ColBERTv2(url='http://20.102.90.50:2022/wiki17_abstracts')(query, k=3)
    return [x['text'] for x in results]


def search_wikipedia_react(query: str):
    """This function searches Wikipedia for a given query and returns the top 3 results."""

    lm = dspy.LM('openai/gpt-4o-mini', api_key = os.getenv("OPENAI_API_KEY"))
    dspy.configure(lm=lm)

    react = dspy.ReAct("question -> answer: str", tools=[search_wikipedia])

    pred = react(question=query)
    return pred.answer
