## Natural Language to SQL AI Assistant

## 🧐 Overview

This project is a Streamlit web application that acts as a natural language query assistant for a PostgreSQL database. It allows users to ask questions in plain English, which are then translated into SQL queries by an AI agent. The agent executes the queries and returns the results in a conversational format.

## ✨ Features

- **Natural Language Querying**: Ask questions in plain English to get data from the database.
- **AI Agent Integration**: Uses LangChain and a local LLM to reason, plan, and execute SQL queries.
- **Conversational Memory**: Maintains chat history to answer follow-up questions.
- **Local Deployment**: Runs entirely locally using LM Studio for the LLM and a PostgreSQL database.

## 🛠️ Technology Stack

- **Python 🐍**
- **Streamlit**: For the interactive web application UI.
- **LangChain**: The framework for building the AI agent and its tools.
- **LLM**: A large language model run locally using LM Studio.
- **SQLAlchemy**: The Python SQL toolkit for database interaction.

### 🚀 Getting Started

#### Prerequisites

- Python 3.8 or higher
- PostgreSQL
- pip (Python package manager)

#### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sidd475/natural-language-sql.git
   cd sql_nlp
   ```
2.Install packages
   ```bash
   uv pip install reqirements.txt
   ```
3.Set up Database
- Update the DATABASE_URL in the environment variables.
- Run the Script
-Set up the database:
   ```bash
   python create_tables.py
   ```
-Seed the Database
   ```bash
   python seed.py
   ```
-Launch the Streamlit app
   ```bash
   streamlit run streamlit_file.py
   ```
4. Set up a PostgreSQL server:
   - Install PostgreSQL if not already installed.
   - Create a new database for the application.
   - Note down the connection details (host, port, username, password, and database name).

5. Add a `.env` file in the repository root with the following keys:
   ```bash
   postgresql://<username>:<password>@localhost:5432/<database_name>
   ```
   -Replace `<username>`, `<password>`, `<host>`, `<port>`, `<database_name>`
6.In `.env` add your llm model name and its key
   ```bash
   MODEL_URL="your_url"
   MODEL_NAME="Model_Name"
   ```
