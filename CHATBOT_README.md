# RAG Chatbot Frontend

A beautiful web interface for your RAG (Retrieval-Augmented Generation) system built with Flask and modern HTML/CSS/JavaScript.

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Make sure your RAG system is ready
- Run your Jupyter notebook (`Notebook/document.ipynb`) first to create the ChromaDB vector store
- Ensure your `.env` file contains your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```

### 3. Start the Chatbot
```bash
python run_chatbot.py
```

Or directly:
```bash
python app.py
```

### 4. Open Your Browser
Navigate to: `http://localhost:5000`

## 🎯 Features

- **Beautiful UI**: Modern, responsive chat interface
- **Real-time Chat**: Instant responses from your RAG system
- **Typing Indicators**: Visual feedback while processing
- **Mobile Friendly**: Works great on all devices
- **Sample Questions**: Built-in suggestions to get started

## 🛠️ How It Works

1. **Frontend**: Clean HTML/CSS/JS chat interface
2. **Backend**: Flask server that connects to your RAG system
3. **RAG Integration**: Uses your existing ChromaDB and LangChain setup
4. **LLM**: Powered by Google Gemini for intelligent responses

## 📁 Project Structure

```
├── app.py                 # Flask backend server
├── templates/
│   └── index.html        # Chat interface
├── run_chatbot.py        # Easy startup script
├── Notebook/
│   ├── document.ipynb    # Your RAG implementation
│   └── chroma_db/        # Vector database
└── requirements.txt      # Dependencies
```

## 🔧 Customization

### Change the Model
Edit `app.py` and modify the LLM initialization:
```python
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",  # Change model here
    temperature=0.1          # Adjust creativity
)
```

### Modify the Prompt
Update the system prompt in `app.py`:
```python
system_prompt = """Your custom prompt here..."""
```

### Styling
Edit `templates/index.html` to customize the appearance.

## 🐛 Troubleshooting

### ChromaDB Not Found
- Make sure you've run your Jupyter notebook first
- Check that `./Notebook/chroma_db/` exists

### API Key Issues
- Verify your `.env` file has `GOOGLE_API_KEY=your_key`
- Or set it as an environment variable

### Port Already in Use
Change the port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Use different port
```

## 💡 Sample Questions

Try asking your chatbot:
- "How many days can I work remotely?"
- "What are the Aurora X1 headphone specifications?"
- "How do I create a charge using the payments API?"
- "What events are captured in audit logs?"

## 🎉 Next Steps

- Add user authentication
- Implement chat history
- Add file upload for new documents
- Deploy to cloud platforms
- Add voice input/output

Enjoy your RAG-powered chatbot! 🤖✨