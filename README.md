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





