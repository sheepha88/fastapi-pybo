from fastapi import APIRouter

from database import SessionLocal
from models import Answer

router = APIRouter(
    prefix="/api/answer"
)


@router.get("/list")
def answer_list():
    db = SessionLocal()
    _answer_list = db.query(Answer).all()
    db.close()
    return _answer_list