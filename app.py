from flask import Flask, request, jsonify
from dotenv import load_dotenv

from langchain_ollama import OllamaLLM
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

app = Flask(__name__)

# Local embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector database
vectorstore = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# GPT model
llm = OllamaLLM(
    model="phi3:mini"

)

@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    question = data.get("message")

    # Retrieve relevant docs
    docs = retriever.invoke(question)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
    You are a helpful presales AI assistant.

    Use the provided context to answer the question.

    Context:
    {context}

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    return jsonify({
    "response": response
})

@app.route("/")
def home():
    return "Presales Chatbot Running Successfully"

if __name__ == "__main__":
    app.run(debug=True)