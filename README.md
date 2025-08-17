Natural Language to SQL AI Assistant

🧐 Overview

This project is a Streamlit web application that acts as a natural language query assistant for a PostgreSQL database. It allows users to ask questions in plain English, which are then translated into SQL queries by an AI agent. The agent executes the queries and returns the results in a conversational format.

✨ Features

    Natural Language Querying: Ask questions in plain English to get data from the database.

    AI Agent Integration: Uses LangChain and a local LLM to reason, plan, and execute SQL queries.

    Conversational Memory: Maintains chat history to answer follow-up questions.

    Local Deployment: Runs entirely locally using LM Studio for the LLM and a PostgreSQL database.

🛠️ Technology Stack

    Python 🐍

    Streamlit: For the interactive web application UI.

    LangChain: The framework for building the AI agent and its tools.

    LLM: A large language model run locally using LM Studio.

    SQLAlchemy: The Python SQL toolkit for database interaction.

    psycopg2: The PostgreSQL database adapter for Python.

🚀 Setup & Installation

1. Prerequisites

    Python 3.10+

    PostgreSQL

    LM Studio

2. Clone the Repository

Bash

git clone <your-repository-url>
cd <your-repository-name>

3. Set Up the Environment

First, create and activate a Python virtual environment.
Bash

python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate

Next, install the required packages:
Bash

pip install -r requirements.txt

4. Configure Environment Variables

Create a file named .env in the project's root directory and add the following content. Replace the placeholders with your actual database credentials and LM Studio URL.
Ini, TOML

DATABASE_URL="postgresql://user:password@localhost:5432/your_database_name"
MODEL_API_BASE="http://localhost:1234/v1"
MODEL_NAME="lm-studio"

Important: Ensure your database user has SELECT privileges on the employees, products, and sales tables. For the initial setup, you might need to grant CREATE and INSERT privileges temporarily to create the tables and seed the data, then revoke them for security.

5. Database Setup

Run the following scripts to create your database tables and populate them with sample data.
Bash

python create_tables.py
python seed.py

🏃 Running the Application

    Start your LM Studio server with your chosen LLM loaded.

    Start the Streamlit application from your terminal.

Bash

streamlit run app/app.py

The application will open in your web browser, and you can start asking questions!
