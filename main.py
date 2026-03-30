from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

class TextRequest(BaseModel):
    text: str

@app.post("/summarize")
def summarize(request: TextRequest):
    try:
        prompt = f"Summarize this:\n{request.text}"

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return {"summary": response.text}

    except Exception as e:
        message = str(e)
        if "429" in message or "RESOURCE_EXHAUSTED" in message:
            raise HTTPException(status_code=429, detail=message)
        raise HTTPException(status_code=500, detail=message)
    #uvicorn main:app --reload # Run the server with this command in the terminal.
