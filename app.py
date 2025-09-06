from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain

# Load environment variables
load_dotenv()

app = Flask(__name__)

class RAGChatbot:
    def __init__(self):
        self.vectorstore = None
        self.rag_chain = None
        self.setup_rag()
    
    def setup_rag(self):
        """Initialize the RAG system"""
        try:
            # Initialize embeddings
            embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
            
            # Load existing ChromaDB
            persist_directory = "./Notebook/chroma_db"
            self.vectorstore = Chroma(
                persist_directory=persist_directory,
                embedding_function=embeddings,
                collection_name="rag_collection"
            )
            
            # Initialize LLM
            llm = ChatGoogleGenerativeAI(
                model="gemini-1.5-flash",
                temperature=0.2
            )
            
            # Create retriever
            retriever = self.vectorstore.as_retriever(search_kwargs={"k": 3})
            
            # Create prompt template
            system_prompt = """You are a helpful assistant for question-answering tasks. 
            Use the following pieces of retrieved context to answer the question. 
            If you don't know the answer, just say that you don't know. 
            Keep the answer concise and helpful.

            Context: {context}"""
            
            prompt = ChatPromptTemplate.from_messages([
                ("system", system_prompt),
                ("human", "{input}")
            ])
            
            # Create document chain
            document_chain = create_stuff_documents_chain(llm, prompt)
            
            # Create RAG chain
            self.rag_chain = create_retrieval_chain(retriever, document_chain)
            
            print("✅ RAG system initialized successfully!")
            
        except Exception as e:
            print(f"❌ Error initializing RAG system: {e}")
            self.rag_chain = None
    
    def get_response(self, question):
        """Get response from RAG system"""
        if not self.rag_chain:
            return "Sorry, the RAG system is not available right now."
        
        try:
            response = self.rag_chain.invoke({"input": question})
            return response["answer"]
        except Exception as e:
            print(f"Error getting response: {e}")
            return "Sorry, I encountered an error while processing your question."

# Initialize chatbot
chatbot = RAGChatbot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data.get('message', '')
    
    if not question.strip():
        return jsonify({'response': 'Please ask a question!'})
    
    response = chatbot.get_response(question)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)