
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CodeInput(BaseModel):
    language: str
    code: str

from llm.reviewer import review_with_llm

@app.post("/review")
def review_code(data: CodeInput):
    llm_review = review_with_llm(data.code, data.language)
    return {"llm_review": llm_review}
