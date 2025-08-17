# app/agent.py
import os

from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from sqlalchemy import create_engine

# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set.")
MODEL_BASE = os.getenv("MODEL_API_BASE")
if not MODEL_BASE:
    raise ValueError("MODEL BASE environment variable not set")
MODEL_NAME = os.getenv("MODEL_NAME")

engine = create_engine(DATABASE_URL)
db = SQLDatabase(engine)
llm = ChatOpenAI(
    model=MODEL_NAME, temperature=0, api_key="Not-needed", base_url=MODEL_BASE
)


def get_answer_from_db(question: str, memory: ConversationBufferMemory):
    # This function creates the agent and runs the query
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful AI assistant that translates natural language to SQL queries and answers questions based on the results. You have access to a database with employees, products, and sales tables.",
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    sql_agent = create_sql_agent(
        llm=llm,
        db=db,
        agent_type="openai-tools",
        verbose=True,
        handle_parsing_errors=True,
        prompt=prompt,
        memory=memory,
    )

    try:
        response = sql_agent.invoke({"input": question, "chat_history": []})
        return response
    except Exception as e:
        return {"output": f"An error occurred: {e}"}


if __name__ == "__main__":
    # This part is for local testing, outside of Streamlit
    questions = [
        "How many employees are there in the 'Sales' department?",
        "What is the average price of products in the 'Electronics' category?",
        "Which employee made the most sales in terms of quantity?",
    ]
    test_memory = ConversationBufferMemory(return_messages=True)

    for q in questions:
        print(f"Question: {q}")
        answer = get_answer_from_db(q, test_memory)
        print(f"Answer: {answer}\n")
