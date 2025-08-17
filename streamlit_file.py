# app.py
import os

import streamlit as st
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory

# Import from your corrected 'app' package structure
from app.agent import get_answer_from_db

# Load environment variables
load_dotenv()

# Streamlit UI
st.title("Natural Language to SQL Query Engine with Chat History")
st.markdown(
    "Ask questions about your database in plain English. The agent will remember the conversation."
)

# Initialize chat history and memory in session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(return_messages=True)

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt_input := st.chat_input("What is your question?"):
    st.session_state.messages.append({"role": "user", "content": prompt_input})
    with st.chat_message("user"):
        st.markdown(prompt_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_answer_from_db(prompt_input, st.session_state.memory)

            # Check for an error message in the response
            if "output" in response and "An error occurred" in response["output"]:
                st.error(response["output"])
                st.session_state.messages.append(
                    {"role": "assistant", "content": response["output"]}
                )
            else:
                sql_query = "SQL query could not be extracted."
                intermediate_steps = response.get("intermediate_steps", [])
                if intermediate_steps:
                    tool_call = intermediate_steps[0]
                    if (
                        isinstance(tool_call, tuple)
                        and hasattr(tool_call[0], "tool_input")
                        and "query" in tool_call[0].tool_input
                    ):
                        sql_query = tool_call[0].tool_input["query"]
                        st.markdown("### Generated SQL Query:")
                        st.code(sql_query, language="sql")

                final_answer = response["output"]
                st.markdown("### Final Answer:")
                st.success(final_answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": f"### Generated SQL Query:\n```sql\n{sql_query}\n```\n### Final Answer:\n{final_answer}",
                    }
                )
