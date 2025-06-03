# RAG with Azure Embedding Model - Famous Places in Tamil Nadu

A Retrieval-Augmented Generation (RAG) application that helps users find famous places in Tamil Nadu based on their queries using Azure OpenAI embeddings and PostgreSQL with pgvector extension.

## 🌟 Features

- **Semantic Search**: Find relevant places using natural language queries
- **Azure OpenAI Integration**: Leverages Azure's embedding models for accurate similarity matching
- **Vector Database**: Uses PostgreSQL with pgvector extension for efficient similarity search
- **RESTful API**: FastAPI-based REST API for easy integration
- **Real-time Results**: Get instant recommendations for places to visit

## 🏗️ Architecture

The application consists of:
- **FastAPI**: Web framework for the REST API
- **Azure OpenAI**: Embedding generation service
- **PostgreSQL + pgvector**: Vector database for similarity search
- **Pandas**: Data processing from Excel files

## 📋 Prerequisites

- Python 3.8+
- PostgreSQL 17.5
- Visual Studio Community 2022 (for pgvector installation on Windows)
- Azure OpenAI API access

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/thirumurugan2001/RAG_with_azure_embedding_model.git
cd RAG_with_azure_embedding_model
```

### 2. Install Python Dependencies

```bash
pip install fastapi uvicorn psycopg2-binary pandas python-dotenv azure-ai-inference openpyxl
```

### 3. Install pgvector Extension

Follow the detailed steps provided in the codebase:

#### Check PostgreSQL Installation
```bash
psql --version
```

#### Install Visual Studio C++ Support
- Download Visual Studio Community 2022
- Select "Desktop development with C++" workload

#### Install pgvector
1. Open Developer Command Prompt for VS 2022 as Administrator
2. Set up Visual Studio environment:
```bash
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"
```

3. Set PostgreSQL root:
```bash
set PGROOT="C:\Program Files\PostgreSQL\17"
```

4. Clone and build pgvector:
```bash
cd %TEMP%
git clone --branch v0.8.0 https://github.com/pgvector/pgvector.git
cd pgvector
nmake /F Makefile.win
nmake /F Makefile.win install
```

5. Enable extension in PostgreSQL:
```bash
psql -U postgres -d your_database_name
CREATE EXTENSION vector;
```

### 4. Environment Configuration

Create a `.env` file in the project root:

```env
# Azure OpenAI Configuration
AZURE_OPENAI_API_KEY=your_azure_openai_api_key
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
MODEL=your_embedding_model_name

# Database Configuration
DATABASE=your_database_name
USER=your_db_username
PASSWORD=your_db_password
HOST=localhost
PORT=5432
```

### 5. Database Setup

1. Create the database table and insert data:
```python
from helper import CreateTable, insert_into_database

# Create table
CreateTable()

# Insert data from Excel file
insert_into_database()
```

Make sure you have the `Famous_Places_Tamil_Nadu.xlsx` file in your project directory.

## 🎯 Usage

### Start the Server

```bash
python main.py
```

The API will be available at `http://0.0.0.0:8080`

### API Endpoint

**POST** `/rag/query`

#### Request Body
```json
{
    "query": "best place to visit in may month like temple in tamil nadu"
}
```

#### Success Response (200)
```json
{
    "data": [
        {
            "place": "Vellore Golden Temple",
            "description": "Known for the Sripuram Golden Temple with intricate gold-coated architecture."
        }
    ],
    "message": "Successfully completed the RAG for your Query",
    "status": true,
    "statusCode": 200
}
```

#### Error Response (400)
```json
{
    "data": [
        {
            "response": "Error message"
        }
    ],
    "message": "Failed to RAG your Query",
    "status": false,
    "statusCode": 400
}
```

## 📁 Project Structure

```
├── main.py                 # FastAPI application entry point
├── model.py               # Pydantic models for request/response
├── helper.py              # Database operations and embedding functions
├── datamainpulation.py    # Similarity search implementation
├── Famous_Places_Tamil_Nadu.xlsx  # Data source
├── .env                   # Environment variables
└── README.md             # Project documentation
```

## 🔧 API Testing

### Using cURL
```bash
curl -X POST "http://0.0.0.0:8080/rag/query" \
     -H "Content-Type: application/json" \
     -d '{"query": "best temple to visit in summer"}'
```

### Using Python requests
```python
import requests

url = "http://0.0.0.0:8080/rag/query"
payload = {"query": "best place to visit in may month like temple in tamil nadu"}
response = requests.post(url, json=payload)
print(response.json())
```

## 🛠️ Development

### Adding New Data
1. Update the Excel file with new places and descriptions
2. Run the data insertion function:
```python
from helper import insert_into_database
insert_into_database()
```

### Database Operations
- **Create Table**: `CreateTable()`
- **Insert Data**: `insert_into_database()`
- **Select Data**: `selectData()`
- **Drop Table**: `dropTable()`

## 🔍 How It Works

1. **Query Processing**: User sends a natural language query
2. **Embedding Generation**: Azure OpenAI generates embeddings for the query
3. **Similarity Search**: PostgreSQL with pgvector finds the most similar place
4. **Response**: Returns the best matching place with description

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support

For support and questions, contact: [thirusubramaniyan2001@gmail.com](mailto:thirusubramaniyan2001@gmail.com)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Azure OpenAI for embedding services
- pgvector for PostgreSQL vector operations
- FastAPI for the web framework
- Contributors and maintainers

---

**Repository**: [https://github.com/thirumurugan2001/RAG_with_azure_embedding_model.git](https://github.com/thirumurugan2001/RAG_with_azure_embedding_model.git)
