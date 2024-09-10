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
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from . import models, schemas

# SQLite 데이터베이스 파일 경로 설정
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./qna.db"

# SQLAlchemy 엔진 생성 (async)
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# 비동기 세션 메이커 생성
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# 모델 초기화
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

# FastAPI 애플리케이션 시작 시 모델 초기화
@app.on_event("startup")
async def startup_event():
    await init_models()

# DB 연결 세션 획득 함수
async def get_db():
    async with async_session() as session:
        yield session


app = FastAPI()


@app.post("/users", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    existed_user = await db.query(models.User).filter_by(
        email=user.email
    ).first()
    # existed_user = db.query(models.User).filter_by(email=user.email).first()

    if existed_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = models.User(email=user.email, password=user.password)
    db.add(user)
    await db.commit()

    return user


@app.get("/users", response_model=List[schemas.User])
async def read_users(db: AsyncSession = Depends(get_db)):
    return await db.query(models.User).all()    

if __name__ == "__main__":
  import uvicorn
  uvicorn.run("main:app", reload=True)
