from pydantic import BaseModel

""" 
Pydantic 모델을 정의한 파일입니다. 
사실, SQLAlchemy와 Pydantic 모두 "모델"이란 용어를 사용합니다. 
그래서 이 둘을 같이 사용할 경우 용어를 정의해야 하는데, 
FastAPI 공식 문서에는 pydantic "model"을 "schema"로 표현해 문제를 해결했습니다.
"""

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    email: str
    is_active: bool

    class Config:        
        # orm_mode = True # Pydantic 이 Alchemy 모델을 사용함.
        from_attributes = True # Pydantic 이 Alchemy 모델을 사용함.