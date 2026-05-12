from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.services.mentor_service import get_ai_feedback
from app.services.db_service import save_journal, get_journals
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="CortexAlpha API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class JournalInput(BaseModel):
    content: str
    style: str = "buffett"
    mood: str = None
    ticker: str = None

@app.get("/")
def root():
    return {"status": "CortexAlpha is running"}

@app.post("/feedback")
async def get_feedback(data: JournalInput):
    feedback = await get_ai_feedback(data.content, data.style)
    saved = await save_journal(data.content, data.style, feedback, data.mood, data.ticker)
    return {"feedback": feedback, "style": data.style, "id": saved["id"]}

@app.get("/journals")
async def list_journals():
    journals = await get_journals()
    return {"journals": journals}