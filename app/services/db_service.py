from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

async def save_journal(content: str, style: str, feedback: str, mood: str = None, ticker: str = None):
    data = {
        "content": content,
        "style": style,
        "feedback": feedback,
        "mood": mood,
        "ticker": ticker
    }
    result = supabase.table("journals").insert(data).execute()
    return result.data[0]

async def get_journals():
    result = supabase.table("journals").select("*").order("created_at", desc=True).execute()
    return result.data