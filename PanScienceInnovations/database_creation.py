import sqlite3
import json
from langchain.schema import Document
from user_query import upload_documents

# Sample list of documents
def create_database_of_metadata(documents_folder_path,documents_folder_name):
    documents = upload_documents(documents_folder_path)

    # Connect to SQLite database (or create it)
    conn = sqlite3.connect("documents_metadata.db")
    cursor = conn.cursor()

    # Create table (if not exists)
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {documents_folder_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT,
        metadata TEXT
    )
    ''')

    # Insert data
    for doc in documents:
        cursor.execute("INSERT INTO documents (content, metadata) VALUES (?, ?)",
                       (doc.page_content, json.dumps(doc.metadata)))

    # Commit and close
    conn.commit()
    conn.close()