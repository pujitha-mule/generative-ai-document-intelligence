# Generative AI Document Intelligence System

A FastAPI application that extracts structured information from text-based PDF documents using an LLM.

## Extracted Fields

- Name
- Date
- Amount
- Category
- Summary

## Features

- PDF upload endpoint
- Text extraction with PyPDF
- LLM-based structured information extraction
- Validated JSON output with Pydantic
- Dockerized deployment
- Swagger/OpenAPI interface

## Architecture

PDF Upload → Text Extraction → Prompt Construction → LLM → JSON Parsing → Pydantic Validation → API Response

## Local Setup

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env`, add your OpenAI API key, then run:

```bash
uvicorn app.main:app --reload
```

Open `/docs` for the Swagger interface.

## Docker

```bash
docker build -t document-intelligence .
docker run --env-file .env -p 8000:8000 document-intelligence
```

## API

- `GET /health`
- `POST /extract`

## Important Limitation

This starter implementation handles PDFs containing machine-readable text. Scanned/image-only PDFs need an OCR layer before extraction.

## Evaluation

If you put an extraction-accuracy percentage on your resume, create a labeled test set and calculate the metric from actual predictions. Do not use an estimated or invented percentage.

## Tech Stack

Python, FastAPI, OpenAI API, PyPDF, Pydantic, Docker
