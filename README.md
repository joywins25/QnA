# Temporary only for QnA  
---
# FastCampus FastAPI Lecture 2021 by Spike H.Y. Lee(이호열)
* URL : https://fastapi.notion.site/dddb1dba1d154834bd7968a8daf89995?v=c35c3464fa3d43b3b65d5cfd75cd84a5 | 

## Chapter01110. FastAPI 설치 및 Pydantic 소개 

* URL : https://fastapi.notion.site/FastAPI-Pydantic-5ba76c8d0a024ceb8137efcebf4d2a9e | FastAPI 설치 및 Pydantic 소개

* FastAPI 는 Python 3.6 에서는 안되므로 Python 3.10 환경에서 실습합니다.


### Anaconda 가상환경을 이용한 환경파일 생성 및 복원 관련 명령어 정리 : 

* 가상환경 생성 및 환경파일 생성 및 복원 명령어 : 
```
conda create --name py31064_fastselenistreamlit --clone py310_64_streamlit
conda activate py31064_fastselenistreamlit

(py31064_fastselenistreamlit) C:\Joywins\TechArchive\TechArchive_Python_FastAPI\Ex004_FastCampus_FastAPI>

# 가상환경 목록 파일 생성 :
# 1. conda 로 설치된 패키지만 환경 파일로 생성하는 방법 :

# 1.1. conda로 설치된 패키지만 포함하는 명시적 사양 txt 파일 생성 (가장 권장됨)
# 명시적 사양을 포함한 환경 파일 생성 (플랫폼 간 이식성이 가장 좋음)
# 가장 정확하고 이식성이 좋지만, 사람이 읽기에는 덜 직관적일 수 있습니다.
1.1. conda list --explicit > my_environment_explicit.txt

# 1.2. '--from-history' 옵션을 사용하여 conda로 직접 설치한 패키지만 포함하는 환경 파일 생성 : 
# --from-history 옵션:
# 이 옵션은 사용자가 conda 로 직접 설치한 conda 패키지와 그 버전만 포함하고
# 자동으로 설치된 의존성과 pip로 설치한 패키지는 누락됩니다.
# 따라서 conda와 pip 모두로 설치한 모든 의존성을 포함하려면 이 옵션을 사용하지 않아야 합니다.
# 운영 체제 간 이식성을 고려할 때는 --from-history 옵션이나 --explicit 옵션을 사용하는 것이 좋습니다.
1.2. conda env export -n py31064_fastselenistreamlit --from-history > my_environment_conda_only.yml
1.2. conda env export -n py31064_fastselenistreamlit "--from-history" > my_environment_conda_only.yml


# 2. conda 와 pip 로 설치된 패키지 모두를 목록으로 출력하는 환경 파일로 생성하는 방법 :
# 환경의 모든 세부 정보를 캡처하지만, 플랫폼 종속적일 수 있습니다.

# 2.1. 현재 활성화된 환경을 기준으로 생성합니다.
2.1. conda env export > my_environment_all.yml

# 2.2. 특정한 환경을 지정해서 가상환경 목록 파일을 생성합니다.
2.2. conda env export -n py31064_fastselenistreamlit > my_environment_all.yml


# 3. 환경을 업데이트하려면, yml 파일을 수정한 후 다음 명령을 사용합니다 :
3. conda env update -f environment.yml
```

* 가상환경 환경파일을 이용한 가상환경 복원 생성하기 : 
```
# 1.1. conda로 설치된 패키지만 포함하는 명시적 사양 txt 파일 생성 (가장 권장됨)
1.1. conda create --name new_env_name --file my_environment_explicit.txt

# 2.1. yml 파일을 이용한 환경 생성 :
# 2.1.1. 기본적으로 yml 파일의 name 필드 사용
conda env create -f my_environment_conda_only.yml
# 2.1.2. 또는 특정 이름으로 환경 생성:
conda env create -f my_environment_conda_only.yml -n new_env_name

# 3. conda 와 pip 로 설치된 패키지 모두를 목록으로 출력하는 환경 파일로 생성하는 방법 :
# 3.1. conda 환경 생성하고 환경 활성화하기 :
conda env create -f my_environment_all.yml
conda activate new_env_name
# 3.2. yml 파일외에 'pip freeze > requirements.txt' 로 설치된 패키지를 목록을 가진 txt 파일이 있는 경우 :
#    conda 로 생성한 의존성만 목록이 있는 'environment.yml' 파일을 이용하여 conda 환경을 먼저 생성한 후 
#    pip 로 생성한 의존성만 목록이 있는 'requirements.txt' 파일을 이용하여 pip 환경을 생성합니다.
3.2. pip install -r requirements.txt
```

### 실습 파일 : Ex004_FastCampus_FastAPI\main.py

### 라이브러리 설치 :
```
pip install fastapi
pip install uvicorn
```
---

## Chapter01120. 경로 매개변수

### 라이브러리 설치 : 
* URL : https://httpie.io/ | HTTPie – API testing client that flows with you
```
# 설치 명령 : 
pip install httpie


# 실행 명령 : 

# Ex.01 :
http localhost:8000
HTTP/1.1 200 OK
content-length: 15
content-type: application/json
date: Wed, 14 Apr 2021 13:18:49 GMT
server: uvicorn

"Hello, World!"

# Ex.02 : 
http :8000
```

### 순서 문제 :

* FastAPI에는 몇 안되는 단점이 존재합니다. 
* 바로 경로의 순서 문제입니다. 

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


# 추가: 현재 유저를 반환하는 앤드포인트
@app.get("/users/me")
def get_current_user():
    return {"user_id": 123}
```    


## Chapter01130. 쿼리 매개변수


## Chapter01140. 요청 본문


## Chapter01150. 응답 모델


## Chapter01160. 데이터 검증
* json 을 이용한 body 를 사용하고 간단한 모델일 경우에는 데이터 class 를 이용하는 것 같습니다.


## Chapter01170. 헤더, 쿠키 매개변수
```
GET 방식에서 '?'를 이용하여 전달하는 경우는 쿼리 파라미터이고, '?'를 사용하지 않고 '변수이름:값'의 묶음으로 전달하는 경우는 헤더와 쿠키에서 사용한다고 정리하는 것은 
완전히 정확하지는 않습니다.

따라서, '?' 유무만으로 쿼리 파라미터, 헤더, 쿠키를 구분하는 것은 정확하지 않습니다. 정보가 전달되는 위치와 형태, 그리고 목적에 따라 구분해야 합니다.

혼동되는 부분을 명확히 하면 다음과 같습니다.

* 쿼리 파라미터는 항상 '?' 뒤에 위치합니다. '변수이름:값' 쌍은 '&'로 구분됩니다.

   예: http://example.com/search?q=keyword&page=2


* 헤더는 HTTP 요청 메시지의 일부이며, URL에 직접 나타나지 않습니다. 
  '변수이름:값' 쌍으로 구성되며, 각 쌍은 줄 바꿈으로 구분됩니다.
  요청/응답에 대한 메타데이터를 전달합니다.

  예:GET /header HTTP/1.1
    Host: localhost:8000
    X-Token: some.secret.token

* 쿠키는 헤더를 통해 전달되지만, 사용 목적과 형태가 다릅니다. 
  쿠키는 '변수이름=값' 쌍으로 구성되며, 세미콜론(';')으로 구분됩니다.
  쿠키: 헤더를 통해 전달되지만, 사용자 정보 저장 및 세션 관리 등에 사용됩니다.  

  예: http :8000/cookie Cookie: name=John; session_id=12345
```

## Chapter01200. 도커사용하기
* docker/getting-started 라는 이미지를 pull 받고 백그라운드 모드(-d: detached)로 
  80번 포트(-p 80:80; 포트는 <로컬 호스트 포트>:<컨테이너 포트>)를 연결해서 실행합니다. 
* 원래는 pull 명령을 받아야 하지만 run 명령이 로컬에 해당 이미지가 없다면 도커 허브에서 자동으로 pull 합니다.
```
$ docker run -d -p 80:80 docker/getting-started
```

* 다운로드 받은 docker 이미지들을 조회하고, mysql 을 업데이트합니다.
```
$ docker images

(py31064_fastselenistreamlit) C:\Joywins\TechArchive\TechArchive_Python_FastAPI\Ex004_FastCampus_FastAPI>docker images
REPOSITORY               TAG       IMAGE ID       CREATED         SIZE
mysql                    8.0       7cd8c3640577   6 weeks ago     573MB
docker/getting-started   latest    3e4394f6b72f   20 months ago   47MB

(py31064_fastselenistreamlit) C:\Joywins\TechArchive\TechArchive_Python_FastAPI\Ex004_FastCampus_FastAPI>docker pull mysql:8.0
8.0: Pulling from library/mysql
Digest: sha256:c253b12ccf0c8b291af74f49cb7871bd822a0c71fb6d53d2e1c9f21b5f09b2a4
Status: Image is up to date for mysql:8.0
docker.io/library/mysql:8.0
```

* 실행이 잘 되었는지 확인 할 수 있습니다.
   + 만약 터미널에서 아래 명령어로 실행해서 출력은 되는데 브라우저에 'http://localhost' 주소로 아무것도 뜨지 않으면
     Docker GUI :: Containers 에 running 중인 컨테이너가 조회되고, 
     해당 컨테이너의 Ports 를 클릭하면 'http://localhost/tutorial/' 가 브라우저에 뜹니다.
```
$ docker ps
or
$ docker conatiner ls
```

* 도커의 장점들 : 
   + 도커는 배포를 위해 이미지를 빌드하기도 하지만, 
   + 다른 사람이 빌드한 이미지를 설치 없이 바로 사용할 수 있다는 장점이 있습니다. 

* 설치없이 MySQL 컨테이너 이미지를 받아서 사용하기  
   + MySQL **컨테이너 이미지**를 'fastapi-mysql' 이라는 이름으로 받아서 호스트에서 설치 없이 사용해 보겠습니다.  
```
# `--name`: 컨테이너 이름. 저는 `fastapi-mysql`라고 지었습니다.
# `-e`: 환경 변수
# `-d`: 백그라운드 모드(Detached mode)
# `mysql:8.0`: 이미지 이름.
$ docker run --name fastapi-mysql -e MYSQL_ROOT_PASSWORD=1234 -d mysql:8.0 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
```

* 설치가 잘 되어 잘 실행되는지 조회합니다.
```
$ docker ps
```

* fastapi-mysql 컨테이너을 실행하고 bash 를 실행해서 리눅스 명령어를 몇개 사용하고 종료합니다.
```
$ docker exec -it fastapi-mysql bash

(py31064_fastselenistreamlit) C:\Joywins\TechArchive\TechArchive_Python_FastAPI\Ex004_FastCampus_FastAPI>docker exec -it fastapi-mysql bash
bash-5.1# pwd
/
bash-5.1# ls
afs  bin  boot  dev  docker-entrypoint-initdb.d  entrypoint.sh  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
bash-5.1# exit
exit

(py31064_fastselenistreamlit) C:\Joywins\TechArchive\TechArchive_Python_FastAPI\Ex004_FastCampus_FastAPI>
```

* fastapi-mysql 을 실행하고 패스워드를 입력하고 mysql 을 실행해서 사용하고 종료합니다.
```
$ docker exec -it fastapi-mysql mysql -uroot -p
Enter password:

(py31064_fastselenistreamlit) C:\Joywins\TechArchive\TechArchive_Python_FastAPI\Ex004_FastCampus_FastAPI>docker exec -it fastapi-mysql mysql -uroot -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.39 MySQL Community Server - GPL
...

mysql> show databases;
mysql> use mysql;
mysql> select usr, host from user;
mysql> exit
Bye

(py31064_fastselenistreamlit) C:\Joywins\TechArchive\TechArchive_Python_FastAPI\Ex004_FastCampus_FastAPI>
```


## Chapter01210. RDB 연동
* 파일 4개로 나누기 :
  - main.py
  - database.py: SQLAlchemy 설정
  - models.py: SQLAlchemy Models
  - schemas.py: Pydantic Models

* 라이브러리 설치 : 
```
$ pip install PyMySQL
$ pip install sqlalchemy
$ pip install cryptography
```  

* MySQL 데이터베이스가 켜져 있어야 합니다.
   + 이전 단원의 Docker 실행 명령어가 실행되어 있거나 
     저자가 제공한 깃헙 파일의 쉘파일을 참고하여 실행해야 합니다.
     URL : https://github.com/hard-coders/fastcampusapi/blob/main/tutorial_app/init-db.sh
        - Windows OS 에서는 '^'기호를 이용하여 줄바꿈한다는데 
          운영체제에 맞게 실행이 되는지 확인하고 실행할 필요가 있습니다.
```
#!/bin/sh

docker run -d --name fastapi-mysql \
    -p 3306:3306 \
    -e MYSQL_ROOT_PASSWORD=1234 \
    -e MYSQL_DATABASE=dev \
    -e MYSQL_USER=admin \
    -e MYSQL_PASSWORD=1234 \
    mysql:8.0 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
```
     