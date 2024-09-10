""" 
1. `create_engine` 함수를 이용해 DB 연결할 엔진 생성

    이 코드는 SQLAlchemy 라이브러리를 사용하여 MySQL 데이터베이스에 연결하는 방법을 보여줍니다. 
    
        mysql+pymysql: SQLAlchemy가 MySQL 데이터베이스에 연결하기 위해 사용할 Dialect (pymysql)를 지정합니다.
        admin: MySQL 데이터베이스에 연결할 때 사용할 사용자 이름입니다.
        1234: 해당 사용자의 비밀번호입니다.
        0.0.0.0: 데이터베이스 서버의 주소입니다. 0.0.0.0은 현재 컴퓨터의 모든 IP 주소를 나타내므로, Docker 환경에서 컨테이너 내부에서 호스트 컴퓨터의 MySQL 서버에 접속할 때 유용합니다.
        3306: MySQL 서버의 기본 포트 번호입니다.
        /dev: 연결하려는 데이터베이스의 이름입니다.
        
    즉, 이 코드는 pymysql 드라이버를 사용하여 0.0.0.0:3306에 위치한 MySQL 서버에 admin 사용자로 연결하고, 
    dev라는 이름의 데이터베이스를 사용하도록 설정하는 것입니다.

    만약 다른 데이터베이스를 사용하고 싶다면 /dev 부분을 원하는 데이터베이스 이름으로 변경하면 됩니다.

2. `sessionmaker` 함수를 이용해 세션 생성

3. `declarative_base` 함수는 모델 정의를 위한 부모 클래스 생성

    declarative_base() 함수 :

        SQLAlchemy ORM을 사용하기 위한 기본 설정을 포함하는 베이스 클래스를 생성합니다. 
        이 베이스 클래스를 상속받아 데이터베이스 테이블을 나타내는 Python 클래스를 정의합니다.

    Base 클래스의 역할 :

        Base 클래스는 SQLAlchemy ORM의 핵심 기능을 제공합니다.
        이 클래스를 상속받아 생성된 Python 클래스는 데이터베이스 테이블과 매핑됩니다.
        Base 클래스는 테이블 생성, 데이터 삽입, 조회, 수정, 삭제 등의 데이터베이스 작업을 수행하는 메서드를 제공합니다.
"""


from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite 데이터베이스 파일 경로 설정
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./qna.db"

# SQLAlchemy 엔진 생성
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# 세션 만들기 (async)
async def get_db():
    async with async_session() as session:
        yield session

# 비동기 세션 메이커 생성
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()
