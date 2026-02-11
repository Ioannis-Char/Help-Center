from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import openai
import os

os.environ['OPENAI_API_KEY'] = 'YOUR_API_KEY'



client = OpenAI()


app = FastAPI()


openai.api_key = "YOUR_API_KEY"

#documentation file for reading all information about your site (buttons, actions, choices)
# Ανάγνωση πολλαπλών αρχείων τεκμηρίωσης κατά την εκκίνηση του server
documentation_files = [
    'all_banners_documentation.txt',
    'announcements_documentation.txt',
    'brainstorming_documentation.txt',
    'documentation.txt',
    'information_icons_documentation.txt',
    'question_documentation.txt'
]


all_documentation = ""

for file_path in documentation_files:
    try:
        with open(file_path, 'r') as file:
            all_documentation += file.read() + "\n\n"  # Συνδυασμός περιεχομένων
    except FileNotFoundError:
        print(f"File {file_path} not found.")


# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # spesific domains for safety
    allow_credentials=True,
    allow_methods=["*"],  # allows (GET, POST, etc.)
    allow_headers=["*"],  # allows all headers
)

class Query(BaseModel):
    question: str

def create_prompt(documentation_path, question, role_instructions):
    """
    Generates a prompt for OpenAI API using documentation file and user's question.
    """
    try:
        with open(documentation_path, 'r') as file:
            documentation = file.read()
    except FileNotFoundError:
        return "Documentation file not found."

    prompt = f"""
    You are a specialized assistant who fully understands Conferience, an event management application.

    {role_instructions}

    Documentation:
    {documentation}

    Question:
    {question}

    Answer:
    """
    return prompt

@app.post("/ask")
async def ask_question(query: Query):
    
    role_instructions = "Answer the question based on the provided documentation."
    prompt = create_prompt(documentation_path, query.question, role_instructions)

    if prompt == "Documentation file not found.":
        raise HTTPException(status_code=404, detail="Documentation not found")

    try:
        
        response = client.chat.completions.create (
              model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a specialized assistant who fully understands Conferience, an event management application."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=600,
            temperature=0.7
        )
        
        print(response.choices[0].message.content)
          
        return{response.choices[0].message.content}
   
    except Exception as e:

      print(f"Error occurred: {e}")
      raise HTTPException(status_code=500, detail="An error occurred while processing the request.")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
