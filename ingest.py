from dotenv import load_dotenv
load_dotenv()

import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

DATA_PATH = "data"

all_text = ""

for file in os.listdir(DATA_PATH):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(DATA_PATH, file)

        print(f"Loading {file}")

        loader = PyPDFLoader(pdf_path)

        pages = loader.load()

        print(f"Pages loaded: {len(pages)}")

        for page in pages:

            if page.page_content:

                all_text += page.page_content + "\n"

print(f"\nTotal text length: {len(all_text)}")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

texts = text_splitter.split_text(all_text)

print(f"Created {len(texts)} chunks")

if len(texts) == 0:
    raise ValueError("No text chunks created.")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_texts(texts, embeddings)

vectorstore.save_local("vectorstore")

print("Vector database created successfully")