from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from fastapi import HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database.models import Link
from app.core.database.database import get_db
from app.core.config import HOST

from pydantic import HttpUrl, BaseModel
import random


class HttpStyle(BaseModel):
    link: HttpUrl

link_router = APIRouter()

@link_router.post("/get-short")
def get_short(link: HttpStyle, db: Session = Depends(get_db)):
    try:

        repeat = True
        while repeat:
            uuid = random.randint(1_000_000, 9_999_999)
            exist = db.query(Link).filter(Link.short_code==uuid).first()
            if not exist:
                repeat = False

        short_url = str(HOST)+str(uuid)
        new_link = Link(original_url=str(link.link), short_code=uuid, short_url=short_url)
        db.add(new_link)
        try:
            db.commit()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=f"Internal Error : {e}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Error : {e}")

    finally:
        db.close()

    return {'your short url': short_url}



@link_router.get("/{uid}")
def goto_shorted(uid: int, db: Session = Depends(get_db)):
    try:
        print(uid)
        link = db.query(Link).filter(Link.short_code==uid).first()
        if link is None:
            raise HTTPException(
                status_code=404,
                detail="Short URL not found"
            )
    finally:
        db.close()

    return RedirectResponse(url=link.original_url)