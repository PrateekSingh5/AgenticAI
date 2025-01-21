"""Run `pip install duckdb` to install dependencies."""

import json
from phi.model.openai import OpenAIChat
from phi.agent.duckdb import DuckDbAgent
import openai 
from phi.model.groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key=os.getenv('OPENAI_API_KEY')



from phi.agent import Agent
from phi.tools.duckdb import DuckDbTools

agent = Agent(
    model=Groq(id='llama-3.3-70b-versatile'),
    tools=[DuckDbTools()],
    show_tool_calls=True,
    system_prompt="Use this file for Movies data: /crime_data.csv",
)
agent.print_response("What is the total number number of crimes?", markdown=True, stream=False)
