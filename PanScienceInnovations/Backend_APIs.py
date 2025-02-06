from user_query import upload_documents,store_embeddings_create_retriever,answering_user_queries
from fastapi import FastAPI
from pydantic import BaseModel
from database_creation import create_database_of_metadata
import uvicorn
import sqlite3

class Uploaddocumentrequest(BaseModel):
    documents_folder_path : str

class Userqueryrequest(BaseModel):
    documents_folder_path : str
    query : str

class Uploadindatabase(BaseModel):
    documents_folder_path : str
    documents_folder_name : str
    database_query: str

app = FastAPI(title="Answering User Queries")

@app.post("/uploaddocuments")
def upload_documents(request : Uploaddocumentrequest):
    documents_folder_path = request.documents_folder_path
    response = upload_documents(documents_folder_path)
    return response


@app.post("/queryingsystem")
def querying_system(request : Userqueryrequest):
    documents_folder_path = request.documents_folder_path
    query = request.query
    response = answering_user_queries(documents_folder_path,query)
    return response


@app.post("/viewingmetadata")
def viewing_metadata(request : Uploaddocumentrequest):
    documents_folder_path = request.documents_folder_path
    documents_folder_name = request.documents_folder_name
    database_query = request.database_query

    create_database_of_metadata(documents_folder_path,documents_folder_name)
    conn = sqlite3.connect("documents.db")
    cursor = conn.cursor()
    cursor.execute(database_query)
    rows = cursor.fetchall()
    conn.close()

    return rows



if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=9999)



