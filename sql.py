from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini Function
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-2.0-flash-lite")  # FIXED MODEL NAME

    full_prompt = f"{prompt}\nUser Question: {question}"

    response = model.generate_content(full_prompt)  # FIXED (single string)
    return response.text.strip()

# SQL Function
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    try:
        cur.execute(sql)
        rows = cur.fetchall()
    except Exception as e:
        rows = [(f"SQL Error: {e}",)]

    conn.close()
    return rows

# Prompt definition
prompt = """
You are an expert in converting English questions to SQL queries.
The SQL database has a table STUDENT(Name, Class, Section).

Rules:
- Return only the SQL query.
- Do NOT include ``` or the word "SQL".
"""

# Streamlit UI
st.set_page_config(page_title="I can Retrieve Any SQL Query")
st.header("Gemini → SQL → Database App")

question = st.text_input("Ask your question:", key="input")

submit = st.button("Submit")

if submit:
    sql_query = get_gemini_response(question, prompt)

    st.subheader("Generated SQL Query:")
    st.code(sql_query)

    result = read_sql_query(sql_query, "student.db")
    print(result)
    st.subheader("Query Result:")
    st.write(result)
