#!/usr/bin/env python3
"""
Simple script to run the RAG chatbot
"""
import os
import sys
import subprocess

def check_requirements():
    """Check if required packages are installed"""
    try:
        import flask
        import langchain
        import chromadb
        print("✅ All required packages found!")
        return True
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("Please install requirements: pip install -r requirements.txt")
        return False

def check_chromadb():
    """Check if ChromaDB exists"""
    chroma_path = "./Notebook/chroma_db"
    if os.path.exists(chroma_path):
        print("✅ ChromaDB found!")
        return True
    else:
        print(f"❌ ChromaDB not found at {chroma_path}")
        print("Please run your Jupyter notebook first to create the vector database.")
        return False

def check_env():
    """Check environment variables"""
    if os.path.exists('.env'):
        print("✅ .env file found!")
        return True
    else:
        print("⚠️  .env file not found. Make sure you have your Google API key configured.")
        return True  # Not critical, might be set elsewhere

def main():
    print("🚀 Starting RAG Chatbot...")
    print("=" * 50)
    
    # Check all requirements
    if not check_requirements():
        sys.exit(1)
    
    if not check_chromadb():
        sys.exit(1)
    
    check_env()
    
    print("=" * 50)
    print("🎉 All checks passed! Starting the web server...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 50)
    
    # Run the Flask app
    try:
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Chatbot stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error starting chatbot: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()