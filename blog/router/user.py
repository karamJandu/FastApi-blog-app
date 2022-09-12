from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from .. import schemas, models, hashing
from ..database import get_db
from ..controller import user

router = APIRouter(prefix="/user", tags=["User"])


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(id, db)