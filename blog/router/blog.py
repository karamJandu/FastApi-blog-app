from fastapi import APIRouter, Depends, status, HTTPException, Response
from typing import List
from sqlalchemy.orm import Session

from blog.oAuth2 import get_current_user

from .. import schemas, models
from ..database import get_db
from ..controller import blog
from .. import oAuth2

router = APIRouter(prefix="/blog", tags=["Blog"])

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oAuth2.get_current_user)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.BlogBase, db : Session = Depends(get_db), current_user: schemas.User = Depends(oAuth2.get_current_user)):
   return blog.create(request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oAuth2.get_current_user)):
    return blog.show(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.BlogBase, db: Session =  Depends(get_db), current_user: schemas.User = Depends(oAuth2.get_current_user)):
    return blog.update(id, request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oAuth2.get_current_user)):
    return blog.destroy(id, db)
