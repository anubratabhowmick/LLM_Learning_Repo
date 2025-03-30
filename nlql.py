import argparse
import openai
import os
import re
import sqlite3
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_table_schema(dbpath):
    """
    Extract the table schema from the database.
    
    Args:
        dbpath (str): The path to the database file
    Returns:
        create_table_statements (list): A list of create table statements
    """
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute("SELECT sql FROM sqlite_master WHERE type='table';")
    create_table_statements = cursor.fetchall()
    table_cells = [row[0] for row in create_table_statements]
    conn.close()
    return '\n'.join(table_cells)


def process_question(dbpath, question):
    """
    Process the question to be a valid query on SQLite database   
    Args:
        dbpath (str): The path to the database file
        question (str): The question to process
    Returns:
        question (str): The processed question
    """
    conn = sqlite3.connect(dbpath)  
    cursor = conn.cursor()
    cursor.execute(question)
    rows = cursor.fetchall()
    rows = [str(row) for row in rows]
    conn.close()
    return '\n'.join(rows)


def create_prompt(question, db_structure):
    """
    Create a prompt for the text-to-SQL translation.
    
    Args:
        question (str): The question to translate to NLQL
    Returns:
        prompt (str): The prompt for the text-to-SQL translation
    """
    parts = []
    parts.append('Database:')
    parts.append(db_structure)
    parts.append('Translate this question to SQL:')
    parts.append(question)
    
    return '\n'.join(parts)

def call_LLM(prompt):
    """
    Call the LLM with the prompt.
    
    Args:
        prompt (str): The prompt for the text-to-SQL translation
    Returns:
        response (str): The response from the LLM
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}])
    
    return response.choices[0].message.content

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Table Retrieval")
    parser.add_argument("--dbpath", type=str, help="Database file path")
    # parser.add_argument("--question", type=str, help="Question to translate to NLQL")
    args = parser.parse_args()
    
    db_structure = extract_table_schema(args.dbpath)
    
    while True:
        question = input('Enter Question: ')
        
        if question == 'exit':
            break
        
        prompt = create_prompt(question, db_structure)
        print('---PROMPT---')
        print(prompt)
        print('\n\n')
        
        response = call_LLM(prompt)
        answer = re.findall(r'```sql(.*)```', response, re.DOTALL)[0]
        print('---QUERY---')
        print(answer)
        
        result = process_question(args.dbpath, answer)
        print('---PROCESSED QUERY---')
        print(result)
        print('\n\n')
