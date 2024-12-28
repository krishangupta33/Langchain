# Langchain Use Cases: RAG, Chatbots, and More

## Description
This project demonstrates various applications of Langchain, showcasing its versatility in building sophisticated AI-driven solutions. Each component is designed to be independent, allowing you to explore different aspects of Langchain's capabilities, from basic chatbots to complex RAG implementations.

## Project Structure

The project consists of six independent modules:

### 1. Agents
- **Purpose**: Demonstrates the power of `agent_executor` in routing queries to appropriate data sources
- **Features**:
  - Dynamic query routing to Wikipedia and Arxiv
  - Intelligent source selection based on query content
  - Integration with multiple data archives
- **Key Components**:
  - Agent executor implementation
  - Wikipedia API integration
  - Arxiv API integration

### 2. API Integration
- **Purpose**: Production-ready API deployment using modern frameworks
- **Technology Stack**:
  - Llama3 LLM model
  - FastAPI for backend services
  - Streamlit for user interface
  - Langchain for LLM orchestration
- **Features**:
  - RESTful API endpoints
  - Interactive web interface
  - Real-time model inference

### 3. Chatbots
- **Purpose**: Implementation of various chatbot architectures
- **Models**:
  - Llama-based chatbot
  - ChatGPT-based chatbot
- **Features**:
  - Context management
  - Conversation history
  - Model-specific optimizations

### 4. Groq Integration
- **Purpose**: High-performance token processing demonstration
- **Features**:
  - Integration with Groq API
  - Mixtral 7B model implementation
  - Performance benchmarking
- **Benefits**:
  - Faster token processing
  - Efficient model inference
  - Optimized response generation

### 5. RAG (Retrieval-Augmented Generation)
- **Purpose**: End-to-end RAG implementation
- **Data Pipeline**:
  - Web scraping using Beautiful Soup
  - PDF document processing
  - Text vectorization
- **Vector Databases**:
  - Chroma DB integration
  - FAISS implementation
- **Features**:
  - Multi-source data ingestion
  - Efficient vector storage
  - Semantic search capabilities

### 6. Retriever
- **Purpose**: Demonstration of retrieval mechanisms
- **Features**:
  - Vector database retrieval
  - Implementation of `db.as_retriever()`
  - Query optimization
- **Use Cases**:
  - Document retrieval
  - Semantic search
  - Context augmentation

## Installation

### Prerequisites
- Python 3.8+
- pip package manager
- Virtual environment (recommended)

### Setup Instructions
1. Clone the repository:
```bash
git clone [repository-url]
cd Langchain-1
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Each module can be used independently. Navigate to the respective directory and follow the module-specific instructions:

### Agents
```bash
cd agents
python main.py
```

### API
```bash
cd api
uvicorn main:app --reload
```

### Chatbots
```bash
cd chatbots
python [chatbot_type]_bot.py
```

### Groq
```bash
cd groq
python groq_example.py
```

### RAG
```bash
cd rag
python rag_implementation.py
```

### Retriever
```bash
cd retriever
python retriever_example.py
```

## Dependencies

Key dependencies include:
- langchain
- openai
- llama-cpp-python
- fastapi
- streamlit
- beautifulsoup4
- faiss-cpu
- chromadb
- groq
- arxiv
- wikipedia-api


## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
