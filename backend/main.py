import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    code: str
    language: str

@app.get("/")
def root():
    return {
        "message": "LLM Code Review API is live 🚀",
        "endpoint": "/review"
    }

@app.post("/review")
async def review_code(request: CodeRequest):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a senior software engineer. Review the provided code for bugs, security vulnerabilities, and performance optimizations. Provide a structured response."
                },
                {
                    "role": "user",
                    "content": f"Review this {request.language} code:\n\n{request.code}"
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.2,
        )

        ai_review = chat_completion.choices[0].message.content

        return {
            "static_analysis": "Groq Analysis Active",
            "ai_review": ai_review
        }

    except Exception as e:
        if "429" in str(e):
            raise HTTPException(status_code=429, detail="Rate limit reached. Please wait 60 seconds.")
        raise HTTPException(status_code=500, detail="The AI service is currently unavailable.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
