# PanScienceInnovationsProject

This project is about answering user queries based on a list of documents using gpt-4o-mini as the LLM. This project makes use of modern AI technique called RAG (Retrieval Augumented Generation) to find relevant data from the list of documents and answering user queries based on this relevant data.


Tools I used :

1 - LLM - gpt-4o-mini

2 - PDF Reader - PyPDF2

3 - Text Splitter Model - SemanticChunker(OpenAIEmbeddings())

4 - Embedding Model - text-embedding-ada-002(OpenAI)

5 - Vector Store - Chromadb

6 - Database - sqlite3

7 - API - FastAPI

8 - Containerization - Docker

9 - Local Server Creation - uvicorn



Assumption - Files must be PDF files




Here is the step by step way how I made this project - 

1 - To upload the documents I have created a function called upload_documents. This function takes the path of the folder containing the PDF files.

2 - After taking this path it tranverses across the list of files to select only the PDF files.

3 - It extractes the text from the all the PDF files and chunks them based on the semantic meaning of the text.

4 - The chunked text is stored as a list of documents having metadata as the source of file to which a particular document belong

5 - Then I created embeddings of all the documents of the chunked text using text-embedding-ada-002(OpenAI) model

6 - I created a vector store using Chromadb to store all the embeddings

7 - A retriever is then created to search relevant documents from the list of documents

8 - We now allow our users to query from the documents.

9 - Retriever searches for relevant documents by comparing the embeddings of query with the embeddings of documents.

10 - After we get our relevant documents we hydrate our prompt to our LLM with context having list of relevant documents and query from user

11 - Our LLM respond based on the relevant documents and also gives us the names of the files from which it generated its response

12 - We also creates a table in our database having the list of documents with their metadata everytime we upload new files for user queries


Example - 

![image](https://github.com/user-attachments/assets/e760a462-2d0d-4242-ab88-331c7de016b3)


![image](https://github.com/user-attachments/assets/3900d522-aa46-4bb5-8f65-c54b991461ac)


Backend API integration:

1 - I have created three API endpoints for our backend - http://127.0.0.1:9999/uploaddocuments , http://127.0.0.1:9999/queryingsystem, http://127.0.0.1:9999/viewingmetadata

2 - http://127.0.0.1:9999/uploaddocuments endpoint uploads our files and creates a list of documents with the source of each document

3 - http://127.0.0.1:9999/queryingsystem endpoint answers the queries of the users

4 - http://127.0.0.1:9999/viewingmetadata helps in creating a table in the database containing documents and their metadata everytime we upload new files. It also helps in 
    querying from the database to view our metadata 


API calls outside the project:

1 - We only used OpenAI for our LLMs, Chunking and embedding models.

2 - We have to provide our own api key in the form of OPENAI_API_KEY to access and use these models everytime we make API calls to OpenAI

3 - We made use of Langchain in order to make these API calls and creating our vector database using chromadb



Testing Instructions:

1 - I have provided two files for unit and integaration testing

2 - I these files I have also provided the modules which we have to install for our program.

3 - First we have to insert documents folder in the system containing all our PDF files

4 - In the upload_documents function provide the path to this folder to create list of documents containing the name of the file to which it belongs

5 - In the store_embeddings_create_retriever function provide the document folder path to create embeddings of our documents, store it in chromadb vector store and create a 
    retriever to search for relevant documents

6 - In answering_user_queries function provide the document folder path and user query to answer questions based on relevant documents extracted by the retriever using the 
    user query 
    




