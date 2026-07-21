# 🤖 Generative AI Document Intelligence System

An AI-powered document intelligence application built with **Python, FastAPI, OpenAI API, Pydantic, and Docker** that extracts structured information from unstructured PDF documents and returns validated JSON responses through REST APIs.

The system demonstrates how **Large Language Models (LLMs)** can be integrated with backend APIs to transform unstructured document content into structured, application-ready data.

---

## 🚀 Overview

Organizations frequently process documents such as invoices, receipts, reports, and business records that contain important information in unstructured formats.

This project provides an automated document-processing pipeline that:

1. Accepts PDF documents through a FastAPI endpoint
2. Extracts machine-readable text from the uploaded PDF
3. Sends the extracted content to an LLM with a structured prompt
4. Extracts predefined business fields from the document
5. Parses the LLM response into structured JSON
6. Validates the output using Pydantic
7. Returns the validated result through a REST API

---

## ✨ Key Features

- 📄 PDF document upload through REST API
- 🔍 Automatic text extraction using **PyPDF**
- 🧠 LLM-powered document understanding
- 🎯 Prompt-based structured information extraction
- 📦 Structured JSON response generation
- ✅ Schema validation using **Pydantic**
- ⚡ High-performance REST APIs using **FastAPI**
- 🐳 Dockerized application for reproducible execution
- 📚 Interactive API documentation using **Swagger/OpenAPI**
- 🔐 Environment-based API key configuration

---

## 🧠 Extracted Information

The application currently extracts five structured fields:

| Field | Description |
|---|---|
| `name` | Person, organization, or entity associated with the document |
| `date` | Relevant document or transaction date |
| `amount` | Monetary amount identified in the document |
| `category` | Predicted document/category label |
| `summary` | Concise AI-generated summary of the document |

Example response:

```json
{
  "name": "ABC Technologies",
  "date": "2026-06-15",
  "amount": "₹25,000",
  "category": "Invoice",
  "summary": "Invoice issued by ABC Technologies for software development services."
}
```

---

## 🏗️ System Architecture

```text
                     ┌─────────────────┐
                     │   PDF Document  │
                     └────────┬────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │ FastAPI Upload  │
                     │    Endpoint     │
                     └────────┬────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │ PyPDF Text      │
                     │   Extraction    │
                     └────────┬────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │ Prompt          │
                     │ Construction    │
                     └────────┬────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │   OpenAI LLM    │
                     │   Processing    │
                     └────────┬────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │ JSON Parsing +  │
                     │ Pydantic        │
                     │ Validation      │
                     └────────┬────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │ Structured JSON │
                     │ API Response    │
                     └─────────────────┘
```

### Processing Pipeline

```text
PDF Upload
    ↓
Text Extraction
    ↓
Prompt Construction
    ↓
LLM Processing
    ↓
Structured JSON Generation
    ↓
Pydantic Validation
    ↓
REST API Response
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core application development |
| **FastAPI** | REST API development |
| **OpenAI API** | LLM-powered document understanding |
| **PyPDF** | PDF text extraction |
| **Pydantic** | Response schema validation |
| **Docker** | Containerization |
| **Uvicorn** | ASGI application server |
| **Swagger/OpenAPI** | Interactive API documentation |

---

## 📁 Project Structure

```text
generative-ai-document-intelligence/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation & Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/pujitha-mule/generative-ai-document-intelligence.git
cd generative-ai-document-intelligence
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Configuration

Create a `.env` file in the project root.

You can copy the provided example:

```bash
cp .env.example .env
```

Then configure:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

> Never commit your actual API key to GitHub. The `.env` file should remain excluded through `.gitignore`.

---

## ▶️ Running the Application

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

The application will run locally on port `8000`.

---

## 📚 API Documentation

FastAPI automatically generates interactive API documentation.

After starting the application, open:

```text
http://localhost:8000/docs
```

You can upload PDFs and test the extraction API directly through the Swagger interface.

---

## 🔌 API Endpoints

### Health Check

```http
GET /health
```

Example response:

```json
{
  "status": "ok"
}
```

### Extract Document Information

```http
POST /extract
```

Upload a PDF using `multipart/form-data`.

The API processes the document and returns structured information such as:

```json
{
  "name": "ABC Technologies",
  "date": "2026-06-15",
  "amount": "₹25,000",
  "category": "Invoice",
  "summary": "Invoice for software development services."
}
```

---

## 🐳 Docker Deployment

### Build the Docker image

```bash
docker build -t document-intelligence .
```

### Run the container

```bash
docker run --env-file .env -p 8000:8000 document-intelligence
```

The API will then be accessible on port `8000`.

---

## 🧪 Testing the API

You can test the application through:

- Swagger UI
- Postman
- cURL
- Any REST API client

Example using cURL:

```bash
curl -X POST \
  -F "file=@sample.pdf" \
  http://localhost:8000/extract
```

---

## ⚠️ Current Limitations

The current implementation works with **machine-readable PDF documents**.

Image-only or scanned PDFs require an additional **OCR pipeline** before the extracted content can be processed by the LLM.

Other areas that can be improved include:

- Support for additional document formats
- OCR integration for scanned documents
- Batch document processing
- More advanced document classification
- LLM response evaluation
- Persistent document storage
- Authentication and authorization
- Cloud deployment

---

## 🔮 Future Enhancements

Planned extensions include:

- 🔍 OCR support for scanned PDFs
- 📚 Multi-document processing
- 🧠 RAG-based document question answering
- 📊 Automated extraction evaluation pipeline
- ☁️ AWS deployment
- 💾 Database integration for extracted results
- 🔐 JWT-based API authentication
- 📈 Processing and API monitoring

---

## 💡 What This Project Demonstrates

This project demonstrates practical experience with:

- Building **LLM-powered applications**
- Integrating **LLM APIs with Python**
- Prompt engineering for structured extraction
- Processing unstructured documents
- Building production-style REST APIs with **FastAPI**
- JSON schema validation with **Pydantic**
- API testing and documentation
- Environment-based secret management
- Containerizing AI applications using **Docker**

---

## 👩‍💻 Author

**Pujitha Mule**

AI/ML Engineer | Python | Generative AI | LLMs | RAG

GitHub: github.com/pujitha-mule

LinkedIn: linkedin.com/in/pujitha-mule

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐.
