import os
import PyPDF2
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain.schema import Document
load_dotenv()


def upload_documents(documents_folder_path):
    file_names = os.listdir(documents_folder_path)
    documents = []
    for filename in file_names:
        text = ""
        file_path = os.path.join(documents_folder_path, filename)
        if filename.endswith(".pdf"):
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text()
                    formatted_text = text.replace("\n", " ")
                    text_splitter = SemanticChunker(OpenAIEmbeddings())
                    chunks = text_splitter.split_text(formatted_text)
                    for chunk in chunks:
                        doc = Document(page_content=chunk, metadata={"source": filename})
                        documents.append(doc)

    return documents



def store_embeddings_create_retriever(documents_folder_path):
    embedding_function = OpenAIEmbeddings(model="text-embedding-ada-002",
                                      openai_api_key=os.getenv("OPENAI_API_KEY"))
    documents = upload_documents(documents_folder_path)
    vector_store = Chroma.from_documents(documents = documents,embedding = embedding_function)
    retriever = vector_store.as_retriever()
    return retriever



def answering_user_queries(documents_folder_path,query):
    llm = ChatOpenAI(model_name="gpt-4o-mini")
    retriever = store_embeddings_create_retriever(documents_folder_path)
    relevant_text = retriever.get_relevant_documents(query)

    prompt_template = """
    Answer user queries based on the context given in the documents below. Answers should be relevant,concise and relevant to the 
    context . Return only the answer and nothing else. Always include sources of answer
    context : {context}
    query : {query}
    """

    prompt = PromptTemplate.from_template(prompt_template)
    rag_chain = prompt | llm
    response = rag_chain.invoke({"context":relevant_text,"query":query})
    return response.content




