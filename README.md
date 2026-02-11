# FastAPI OpenAI-based API

This project is a FastAPI-based service that uses OpenAI's GPT-3.5-turbo model to answer user queries based on a provided documentation file.

## Features

- Accepts a user query via a POST request.
- Uses OpenAI's GPT model to generate an answer based on the content of the documentation.
- CORS is enabled for all origins, but you can configure it as needed for security.
- Easily customizable for different use cases or documentation sets.

## Requirements

- Python 3
- FastAPI
- Uvicorn
- Pydantic
- OpenAI Python client library


# Help Center HTML

This project is a web-based Help Center for Conferience, an event management application. It integrates with a FastAPI backend that uses OpenAI's GPT model to answer user questions based on a documentation file.

## Features

- A simple web interface where users can submit questions and receive answers.
- The backend uses FastAPI and the OpenAI GPT-3.5-turbo model to generate responses.
- CORS is enabled to allow requests from the front-end.
- Error handling to ensure users receive feedback even in case of issues.

## Front-End

The front-end is an HTML page that allows users to input a question and view the answer returned from the FastAPI server.

### Front-End Components

- **Question Input:** A text field where users can type their question.
- **Answer Display:** A textarea that shows the answer returned by the backend.
- **Submit Button:** Sends the question to the backend.

## Back-End (FastAPI)

The back-end is a FastAPI service that listens for user questions and queries OpenAI’s GPT-3.5-turbo model, which uses a provided documentation file to generate an answer.

### Endpoints

#### POST `/ask`

- **Request Body:**

  ```json
  {
    "question": "Your question here"
  }


