# FastAPI OpenAI-based API & Help Center

##  Overview

This project consists of two main components:

1. A **FastAPI backend** that uses an OpenAI GPT model to generate answers based on a documentation file.
2. A **web-based Help Center front-end** that allows users to ask questions and receive AI-generated responses.

---

##  Backend (FastAPI)

The backend is built using **FastAPI** and provides an API endpoint that accepts user questions and returns AI-generated answers.

### Features
- Accepts user queries via a **POST request**
- Uses an OpenAI GPT model to generate responses based on a provided documentation file
- CORS enabled to allow communication with the front-end
- Error handling to provide meaningful responses in case of failures

### Endpoint

**POST /ask**

#### Request Body:
```json
{
  "question": "Your question here"
}

