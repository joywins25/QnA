"""
* if __name__ == "__main__": 구문이 없을 때 실행 명령 : 
  uvicorn main:app --reload
  
* 문서 보기 : 
  URL : http://127.0.0.1:8000/docs  
  URL : http://127.0.0.1:8000/redoc 
"""

## Chapter01210. RDB 연동
from typing import List

from fastapi import Depends, FastAPI, HTTPException

from . import models, schemas

from database_sqlite import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existed_user = db.query(models.User).filter_by(
        email=user.email
    ).first()

    if existed_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = models.User(email=user.email, password=user.password)
    db.add(user)
    db.commit()

    return user


@app.get("/users", response_model=List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()
    

if __name__ == "__main__":
  import uvicorn
  uvicorn.run("main:app", reload=True)
