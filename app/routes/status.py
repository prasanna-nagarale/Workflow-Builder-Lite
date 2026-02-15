from fastapi import APIRouter
from app.database import SessionLocal
from app.llm import call_llm
from sqlalchemy import text
import os

router = APIRouter()

@router.get("/status")
def health_status():
    """Check system health"""

    status = {
        "backend": "OK",
        "database": "ERROR",
        "llm_provider": "Groq (Llama 3.3 70B)",
        "llm_key_loaded": False,
        "llm_connection": "ERROR"
    }

    # -------- Database check --------
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))   # 🔧 FIX HERE
        db.close()
        status["database"] = "OK"
    except Exception as e:
        status["database"] = f"ERROR: {str(e)}"

    # -------- LLM key check --------
    groq_key = os.getenv("GROQ_API_KEY")
    status["llm_key_loaded"] = bool(groq_key)

    # -------- LLM connection test --------
    if groq_key:
        try:
            result = call_llm("Reply only with OK")
            if "error" not in result.lower():
                status["llm_connection"] = "OK"
            else:
                status["llm_connection"] = result
        except Exception as e:
            status["llm_connection"] = f"ERROR: {str(e)}"

    return status
