# TechArchive_Python_FastAPI :: Ex003_Jump2FastApiWikiDocs
---

## 가상환경 myapi 활성화 후 라이브러리 설치 
```
pip install fastapi
```

### 가상환경 빠르게 실행하는 배치파일 작성
* 배치 파일 위치를 PATH 환경 변수에 추가하기
   + WIN + R, sysdm.cpl
   + 고급 > 환경변수 > 사용자변수 Path 편집 > 'C:\Joywins\MyEnvs\venvs' 등록하고 확인하기
   
* File : "C:\Joywins\MyEnvs\venvs\myapi.cmd"
```
@echo off
cd C:\Joywins\TechArchive\TechArchive_Python_FastAPI\ignore_me_Ex003
C:\Joywins\MyEnvs\venvs/myapi/scripts/activate
```
* 사용법 : 터미널에서 myapi 입력하고 엔터하면 가상환경 실행됩니다.

## IDE 다운로드
* PyCharm for Python FastAPI at backend
* VS Code for Javascript Svelete at frontend

## Svelte 개발환경 
```commandline
(myapi) C:\Joywins\TechArchive\TechArchive_Python_FastAPI\ignore_me_Ex003>npm create vite@latest frontend -- --template svelte
...
(myapi) C:\Joywins\TechArchive\TechArchive_Python_FastAPI\ignore_me_Ex003\frontend>npm install
```

## FastAPI 서버 실행
* uvicorn main:app --reload


## Svelte 서버 실행
* npm run dev


### [4-01 깃으로 버전 관리하기](https://wikidocs.net/177237)
#### projects/myapi/frontend/.gitignore
* dist 제외


### [4-05 서버 접속 설정](https://wikidocs.net/177243)
#### at AWS Lightsail
* 고정 IP 생성
* 방화벽 설정


### [4-07 파이보 세상에 공개하기](https://wikidocs.net/177245)
#### at AWS Lightsail
* 가상 환경 설정하기
   + sudo apt update
   + ~~sudo apt install python3-venv~~
   + sudo apt-get install python3.10-venv
   + mkdir projects
   + mkdir venvs
   + cd venvs
   + python3 -m venv myapi
   + cd myapi
   + cd bin
   + . activate
   + pip install wheel
   + pip install fastapi
   + pip install "uvicorn[standard]"
   + pip install sqlalchemy
   + pip install alembic
   + pip install "pydantic[email]"
   + pip install "passlib[bcrypt]"
   + pip install python-multipart
   + pip install "python-jose[cryptography]"
---  
##### 가상 환경 설정하기.질문1.
  ```
  sudo apt install python3-venv 명령을 실행하면
  
  Daemons using outdted libraries 제목으로 팝업이 뜨면서
  which services should be restarted? 라고 묻고
  [] network-dispatcher.service
  [] unattended-upgrades.service
  <Ok> <Cancel>
  
  라는 화면이 뜨는데 여기서 어떤거 선택하면 되나요?
  ```
---  
##### 가상 환경 설정하기.답변1.
  안녕하세요, 이것은 Bing입니다. 😊

이 팝업은 python3-venv를 설치할 때 발생할 수 있는 일반적인 문제입니다. 이는 python3-venv가 다른 라이브러리와 충돌하기 때문에 일부 서비스를 재시작해야 한다는 것을 의미합니다¹². 이 경우, 두 서비스 모두 재시작하는 것이 좋습니다. 따라서 network-dispatcher.service와 unattended-upgrades.service를 모두 선택하고 <Ok>를 클릭하면 됩니다.

만약 이 방법으로도 문제가 해결되지 않는다면, 다음과 같은 명령어를 사용하여 python3-venv를 설치할 수 있습니다³:

```bash
sudo apt-get install python3.10-venv
```

이 명령어는 python3.10 버전에 맞는 venv 패키지를 설치합니다. 다른 버전을 사용하고 있다면, 적절하게 변경해야 합니다.

이 답변이 도움이 되었기를 바랍니다. 😊

출처: Bing과의 대화, 2024. 1. 8.
> (1) apt-get install python3-venv is not working - Stack Overflow. https://stackoverflow.com/questions/71394061/apt-get-install-python3-venv-is-not-working.  
> (2) How to install python3.10 virtual environment when python3.10-venv has no installation .... https://stackoverflow.com/questions/75131112/how-to-install-python3-10-virtual-environment-when-python3-10-venv-has-no-instal.  
> (3) Linux : Ubuntu 20.04 : Python 3.9 설치 방법, 예제, 명령어. https://jjeongil.tistory.com/2067.  
> (4) apt - Unable to install python3-venv - Ask Ubuntu. https://askubuntu.com/questions/949393/unable-to-install-python3-venv. 
---

#### API 호출 URL 변경하기
##### at local pc
* projects/myapi/frontend/.env
   + VITE_SERVER_URL=http://고정IP:8000
   + npm install vite --save-dev
   + npm run build
   + git add *
   + git commit -am "api url changed"
   + git push -u origin main

---  
##### .env.production & npm run build
  ```
  .env.production 파일을 생성하면 
  npm run build로 빌드 파일을 생성할 때 
  .env 파일을 참조하지 않고 
  .env.production 파일을 참조하게 된다.
  ```
##### API 호출 URL 변경하기.질문1.
  ```
  npm run build 명령을 실행하면
  
  (py311_fastapi) E:\...\myapi\frontend>npm run build
  
  > frontend@0.0.0 build
  > vite build
  
  'vite'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는
  배치 파일이 아닙니다.
  
  라는 화면이 뜨는데 여기서 어떤거 선택하면 되나요?
  ```
---  
##### API 호출 URL 변경하기.답변1.
   npm install -g vite 을 아래와 같이 전역으로 설치할 수 있으나
   또 다른 오류가 발생하여
   가장 빠른 해결책은 npm install vite --save-dev 로 설치하면 해결됩니다.
   + 참조) npm install -g vite 전역 설치 방법 :
      - 시작 메뉴에서 '시스템 환경 변수 편집' 검색해서'시스템 속성' 창 열기.
      - 시작에서 '시스템 환경 변수 편집’에 들어가 주세요.
      - 시스템 속성→고급→환경 변수에 들어갑니다.
      - 환경 변수 창에서 'Path’로 들어가 vite의 경로를 추가해 주세요. 
         * vite의 경로는 보통 'C:\Users{사용자 이름}\AppData\Roaming\npm\node_modules\vite\bin’입니다.
      - 저장하고 명령 프롬프트를 다시 실행해 보세요.
---


#### 파이보 설치하기
##### at AWS Lightsail
* (myapi) ubuntu@tutorial:~/projects$ git clone https://github.com/joywins25/myapi.git


#### 파이보 실행하기
##### 데이터베이스 초기화하기
###### at AWS Lightsail
* sudo apt install alembic
* (myapi) ubuntu@tutorial:~/projects/myapi$ alembic init migrations  
* (myapi) ubuntu@tutorial:~/projects/myapi$ nano alembic.ini  
   + sqlalchemy.url = sqlite:///./myapi.db
* 
(myapi) ubuntu@tutorial:~/projects/myapi/migrations$ nano env.py
   ```
    import models
    target_metadata = models.Base.metadata
   ```
* (myapi) ubuntu@tutorial:~/projects/myapi$ alembic revision --autogenerate -m "initial migration"  
* (myapi) ubuntu@tutorial:~/projects/myapi$ alembic upgrade head  
   + /home/ubuntu/projects/myapi/myapi.db 파일 생성.


---  
##### 데이터베이스 초기화하기.질문1.

   '가상 환경 설정하기'에서 'pip install alembic' 명령을 실행했으나  
   alembic init migrations 명령을 실행하면   
   아래와 같은 오류가 발생해서 
   ```
    (myapi) ubuntu@tutorial:~/projects/myapi$ alembic init migrations
    Command 'alembic' not found, but can be installed with:
    sudo apt install alembic    
   ```
   
   'sudo apt install python3-venv' 명령을 실행하면   
   ```
      Daemons using outdted libraries 제목으로 팝업이 뜨면서
      which services should be restarted? 라고 묻고
      [] network-dispatcher.service
      [] unattended-upgrades.service
      <Ok> <Cancel>    
   ```  
   라는 화면이 뜹니다.

---

##### 데이터베이스 초기화하기.답변1.A.
   chatgpt 에게 물어보니 둘다 선택하라고 합니다.
   ```
      Daemons using outdted libraries 제목으로 팝업이 뜨면서
      which services should be restarted? 라고 묻고
      [*] network-dispatcher.service
      [*] unattended-upgrades.service
      <Ok> <Cancel>    
   ```  
---  
##### 데이터베이스 초기화하기.답변1.B.
안녕하세요, 이것은 Bing입니다. 😊

이 팝업은 alembic를 설치할 때 발생할 수 있는 일반적인 문제입니다.  
이는 alembic가 다른 라이브러리와 충돌하기 때문에   
일부 서비스를 재시작해야 한다는 것을 의미합니다¹².   
이 경우, 두 서비스 모두 재시작하는 것이 좋습니다.   
따라서 network-dispatcher.service와 unattended-upgrades.service를 모두 선택하고 <Ok>를 클릭하면 됩니다.

만약 이 방법으로도 문제가 해결되지 않는다면,  
다음과 같은 명령어를 사용하여 alembic를 설치할 수 있습니다³:

```bash
sudo apt-get install python3-alembic
```

이 명령어는 python3 버전에 맞는 alembic 패키지를 설치합니다.   
다른 버전을 사용하고 있다면, 적절하게 변경해야 합니다.

이 답변이 도움이 되었기를 바랍니다. 😊

> ¹: [우분투에 pip를 설치하는 과정에서 Daemon using outdated libraries라는 ...](^5^)  
> ²: [linux - How to stop ubuntu pop-up \"Daemons using outdated libraries\" when using apt to install ...](^2^)    
> ³: [alembic package : Ubuntu](^4^)  

출처: Bing과의 대화, 2024. 1. 8.
> (1) 우분투(ubuntu 22.04)에서 needrestart를 설치하고 사용하는 방법. https://sangchul.kr/entry/%EB%A6%AC%EB%88%85%EC%8A%A4-ubuntu-2204-Daemons-using-outdated-librariesneedrestart.  
> (2) How to stop ubuntu pop-up "Daemons using outdated libraries" when using apt to install .... https://stackoverflow.com/questions/73397110/how-to-stop-ubuntu-pop-up-daemons-using-outdated-libraries-when-using-apt-to-i.  
> (3) 우분투에 pip를 설치하는 과정에서 Daemon using outdated libraries라는 .... https://bing.com/search?q=sudo+apt+install+alembic+%eb%aa%85%eb%a0%b9%ec%9d%84+%ec%8b%a4%ed%96%89%ed%95%98%eb%a9%b4+Daemons+using+outdted+libraries+%ec%a0%9c%eb%aa%a9%ec%9c%bc%eb%a1%9c+%ed%8c%9d%ec%97%85%ec%9d%b4+%eb%9c%a8%eb%a9%b4%ec%84%9c+which+services+should+be+restarted%3f+%eb%9d%bc%ea%b3%a0+%eb%ac%bb%ea%b3%a0+%ec%96%b4%eb%96%a4%ea%b1%b0+%ec%84%a0%ed%83%9d%ed%95%98%eb%a9%b4+%eb%90%98%eb%82%98%ec%9a%94%3f.   
---

##### FastAPI 서버 실행하기
###### at AWS Lightsail
* (myapi) ubuntu@tutorial:~/projects/myapi$ sudo apt install uvicorn    
* (myapi) ubuntu@tutorial:~/projects/myapi$ sudo apt install python3-pip  
* (myapi) ubuntu@tutorial:~/projects/myapi$ pip install fastapi  
* (myapi) ubuntu@tutorial:~/projects/myapi$ pip install pydantic[email]  
* (myapi) ubuntu@tutorial:~/projects/myapi$ pip install "python-jose[cryptography]"  
* (myapi) ubuntu@tutorial:~/projects/myapi$ pip install "passlib[bcrypt]"  
* (myapi) ubuntu@tutorial:~/projects/myapi$ pip install python-multipart  

* (myapi) ubuntu@tutorial:~/projects/myapi$ uvicorn main:app --reload --host=0.0.0.0  


### [4-08 서버·개발 환경 분리하기](https://wikidocs.net/177266)
#### at local pc  
##### 환경 파일 작성하기  
* .env
```commandline
    # 4-08 서버·개발 환경 분리하기 :: 환경 파일(.env) 작성하기
    
    # auth
    # import secrets
    # random_hex = secrets.token_hex(8)  # Generate 8 bytes of random data in hexadecimal format
    # print(random_hex)
    # python -c "import os; print(os.urandom(16))"
    SECRET_KEY=b'9\xe0\xd4Wc\x11\x8d\xa0\x07%%_\xeb\x86\xe4\x1b'
    
    # python -c "import secrets; print(secrets.token_hex(8))"
    # _SECRET_KEY='17ff8ff3e480b673'
    
    # 60*24
    ACCESS_TOKEN_EXPIRE_MINUTES=1440
    
    # database
    SQLALCHEMY_DATABASE_URL=sqlite:///./myapi.db
```
  
##### .gitignore 파일에 .env 추가하기
* projects/myapi/.gitignore
   + .env
      - 개발 환경의 .env 파일은 서버에 배포되면 안된다. 


##### .env 파일을 읽어서 사용하기
* projects/myapi/database.py
```python
    from starlette.config import Config
    config = Config('.env')
    SQLALCHEMY_DATABASE_URL = config('SQLALCHEMY_DATABASE_URL')
```  
  + Config 클래스를 사용하면 .env 파일에 설정한 변수의 값을 읽을 수 있다.  
  

* projects/myapi/domain/user/user_router.py
```python
    from starlette.config import Config
        
    (... 생략 ...)
    
    config = Config('.env')
    ACCESS_TOKEN_EXPIRE_MINUTES = int(config('ACCESS_TOKEN_EXPIRE_MINUTES'))
    SECRET_KEY = config('SECRET_KEY')    
```
  
##### 변경 내용 적용하기
* git add .
* git commit -am "4-08 서버·개발 환경 분리하기 :: 변경 내용 적용하기"
* git push -u origin main


#### at AWS Lightsail
##### 운영 환경에 .env 파일 추가하기
* (myapi) ubuntu@tutorial:~/projects/myapi$ git pull
* (myapi) ubuntu@tutorial:~/projects/myapi$ nano .env
```
    # 4-08 서버·개발 환경 분리하기 :: 환경 파일(.env) 작성하기
    
    # auth
    # import secrets
    # random_hex = secrets.token_hex(8)  # Generate 8 bytes of random data in hexadecimal format
    # print(random_hex)
    # python -c "import os; print(os.urandom(16))"
    SECRET_KEY=b'9\xe0\xd4Wc\x11\x8d\xa0\x07%%_\xeb\x86\xe4\x1b'
    
    # python -c "import secrets; print(secrets.token_hex(8))"
    # _SECRET_KEY='17ff8ff3e480b673'
    
    # 60*24
    ACCESS_TOKEN_EXPIRE_MINUTES=1440
    
    # database
    SQLALCHEMY_DATABASE_URL=sqlite:///./myapi.db(myapi) ubuntu@tutorial:~/projects/myapi$
```

* (myapi) ubuntu@tutorial:~/projects/myapi$ uvicorn main:app --reload --host=0.0.0.0

##### 서버에서 가상환경 쉽게 진입하기
```
    개발 환경에서는 myapi.cmd 파일을 이용한 것 처럼
    서버 홈 디렉터리의 .profile 파일에 alias를 추가하여 
    서버 환경에서 가상환경에 쉽게 진입할 수 있는 방법입니다.
```
* /home/ubuntu/.profile 
  + alias myapi='cd ~/projects/myapi;source ~/venvs/myapi/bin/activate'
* sudo reboot
* ubuntu@tutorial:~$ myapi


### [4-09 Gunicorn 사용하기](https://wikidocs.net/177269)
```
    AWS 터미널에서 실행한 다음 명령은 터미널을 종료하면 FastAPI 서버도 종료된다.
        $ uvicorn main:app --reload --host=0.0.0.0

    uvicorn 프로세스를 백그라운드로 실행하면 이를 방지할 수 있다.
     
    대안은 Gunicorn을 사용하면 uvicorn 프로세스를 백그라운드로 실행할 수 있다. 
    Gunicorn은 이외에도 예를 들어 로깅, 서비스 시작, 중지 같은 여러 편의 기능들을 
    Gunicorn 서비스를 등록하여 쉽게 할 수 있다.
    
    Gunicorn은 서버 환경을 위한 도구이므로 로컬 환경에 설치할 필요는 없다.
```

#### at AWS Lightsail
##### Gunicorn 설치하고 사용해 보기
* (myapi) ubuntu@jumpto:~/projects/myapi$ pip install gunicorn
* (myapi) ubuntu@jumpto:~/projects/myapi$ gunicorn --bind 0:8000 main:app --worker-class uvicorn.workers.UvicornWorker

##### Gunicorn 설치하고 사용해 보기
```
    포트 방식으로 Gunicorn을 실행했을 때와 다르다. 
        즉, --bind unix:/tmp/myapi.sock 부분이 다르다. 
        기존에는 --bind 0:8000와 같이 입력했지만 
        유닉스 소켓 방식은 --bind unix:/tmp/myapi.sock와 같이 입력했다.
        
    브라우저에 http://고정IP:8000/ 로 실행하면 다음과 같이 접속이 안됩니다.
        사이트에 연결할 수 없음
        고정IP 에서 연결을 거부했습니다.

    유닉스 소켓 방식으로 실행된 Gunicorn 서버에 접속하기 위해서는 Nginx가 필요하다.
    소켓 방식의 Gunicorn도 정상으로 작동하는 것을 확인한 후에는 
    <Ctrl+C>를 눌러 Gunicorn을 종료하자. 
```
* (myapi) ubuntu@jumpto:~/projects/myapi$ gunicorn --bind unix:/tmp/myapi.sock main:app --worker-class uvicorn.workers.UvicornWorker 


##### Gunicorn 서비스로 등록하기
```
    Gunicorn의 시작, 중지를 쉽게 하고 
    AWS 서버를 다시 시작할 때 Gunicorn을 자동으로 실행하기 위해
    서비스 파일을 생성하여 AWS 서버에 Gunicorn을 서비스로 등록합니다.
```

##### 서비스 파일 생성하기
```
    주의사항 :
    Gunicorn 을 설치하기 위해 
    pip install gunicorn 또는 pip3 install gunicorn 로 설치를 해도
    교재의 'myapi.service' 서비스 파일에서 명시된 경로인 
    '/home/ubuntu/venvs/myapi/bin/gunicorn' 와 다르게
    gunicorn 의 설치 경로가 다른 경우가 발생합니다.
        (myapi) ubuntu@tutorial:~/projects/myapi$ which gunicorn
            /home/ubuntu/.local/bin/gunicorn
                
    이때 '/etc/systemd/system/myapi.service' 파일을 아래와 같이 

        교재 :
            ExecStart=/home/ubuntu/venvs/myapi/bin/gunicorn \ 
        내 소스 :
            ExecStart=/home/ubuntu/.local/bin/gunicorn \
            
    자신의 aws lightsail 가상환경에 gunicorn 이 실제 설치된 경로로 
    수정한 후, 
    서비스 파일이 잘 등록되도록 systemd 를 새로 고침하도록
    'sudo systemctl daemon-reload' 명령을 실행합니다.
```
---

```
    서비스 파일은 시스템 디렉터리에 저장해야 하므로 
    sudo nano myapi.service 명령처럼 
    관리자 권한(sudo)으로 파일을 생성해야 한다.
```
* (myapi) ubuntu@tutorial:/etc/systemd/system$ sudo nano myapi.service
```commandline
    [Unit]
    Description=gunicorn daemon
    After=network.target
    
    [Service]
    User=ubuntu
    Group=ubuntu
    WorkingDirectory=/home/ubuntu/projects/myapi
    ExecStart=/home/ubuntu/.local/bin/gunicorn \
              main:app \
              --workers 2 \
              --worker-class uvicorn.workers.UvicornWorker \
              --bind unix:/tmp/myapi.sock
    [Install]
    WantedBy=multi-user.target
```

* (myapi) ubuntu@tutorial:/etc/nginx/sites-available$ sudo systemctl daemon-reload  
  
  
##### 서비스 실행하고 등록하기
```
    서비스 파일이 관리자 디렉터리에 있으므로 
    실행 역시 관리자 권한으로 실행해야 한다.
    
    'Gunicorn 소켓 사용해 보기' 부분에서 
    "유닉스 소켓 방식으로 실행된 Gunicorn 서버에 접속하기 위해서는 
    Nginx가 필요하다" 라는 설명이 
    서비스 파일을 생성하고 실행한 여기까지도 유효한 이유는 
    서비스 파일 자체가 유닉스 소켓 방식에 관한 설정을 수록했기 때문에
    서비스 파일을 등록하고 난 후에도 
    nginx 가 설치되지 않은 상태이기 때문에 gunicorn 에 접속할 수 없어서 
    웹브라우저에 뜨지 않는 것으로 이해하면 맞을 것 같습니다.
``` 
* (myapi) ubuntu@tutorial:~/projects/myapi$ sudo systemctl start myapi.service
* (myapi) ubuntu@tutorial:~/projects/myapi$ sudo systemctl status myapi.service
   + 만약 정상적인 실행이 안되고 오류 메시지가 나타나면 /var/log/syslog 파일에서  
     오류 원인을 확인하고 수정해야 한다.    
    

* Gunicorn 시작, 종료, 재시작
   + 시작 : sudo systemctl start myapi.service
   + 종료 : sudo systemctl stop myapi.service
   + 재시작 : sudo systemctl restart myapi.service



### [4-10 웹 서버, Nginx 사용해서 파이보에 접속하기](https://wikidocs.net/177311)
```
웹서버(Nginx) ↔ 위스키(WAS, Gunicorn) 간 조작 원칙 :
    파이썬 프로그램을 수정한 경우라면 Gunicorn 을 재시작해야 합니다. 
    엔진엑스를 재기동 해야 하는 경우는 사실 거의 없습니다.
     
    Nginx의 설정을 변경할 경우에만 재기동 하면 됩니다.
```
---
```commandline
문제점 : 
    '4-08 서버·개발 환경 분리하기' 에서
        (myapi) ubuntu@jumpto:~/projects/myapi$ uvicorn main:app --reload --host=0.0.0.0 
            터미널이 살아있는 동안 실행되게 하는 명령까지는 잘 실행되었습니다.  
            
    '4-09 Gunicorn 사용하기' 에서
        sudo systemctl start myapi.service
        sudo systemctl status myapi.service         
            서비스 실행 상태보는 명령까지는 잘 실행되는거 확인했습니다.  
            
    '4-10 웹 서버, Nginx 사용해서 파이보에 접속하기' 에서 
        다음 명령들을 실행하고 모두 문제점이 보이지 않음에도
            sudo systemctl restart nginx
            sudo systemctl daemon-reload
            sudo systemctl status myapi.service
            sudo systemctl status nginx
            sudo nginx -t
        Nginx 설치하고 포트번호 없이 http://고정IP/ 를 입력하면 화면은 뜨지만,
        개발자도구에는 아래와 같은 오류가 발생하면서
        화면만 뜨고 회원가입, 로그인, 목록출력 기능이 안됩니다.
            GET http://고정IP:8000/api/question/list?page=0&size=10&keyword= net::ERR_CONNECTION_REFUSED  

해결책 :
    혹시 몰라서 AWS Lightsail 에서 Sqlite3 다시 설치하고
    frontend/.env.production 파일에서 포트번호를 빼고 
    프론트엔드 빌드를 하고 깃헙 푸쉬한 후,
    AWS Lightsail 터미널에서 깃헙 풀하고
    nginx 재시작하니까 글 목록이 뜹니다.
    
주의사항 :
    frontend/.env.production 파일 수정 작업하고 
    프론트엔드 빌드를 해야해서 
    일단 로컬PC에서 작업해서 깃헙 푸쉬한 후
    AWS Lightsail 터미널에서 깃헙 풀해야 하는 순서에 주의해야 합니다.        
```
---
#### at AWS Lightsail  
##### Nginx 설치  
* (myapi) ubuntu@jumpto:~/projects/myapi$ sudo apt install nginx
   + Nginx를 관리자 권한으로 설치하자.   

##### Nginx 설정  
* cd /etc/nginx/sites-available/
   + /etc/nginx/sites-available은 Nginx의 설정 파일이 위치한 디렉터리이다.  
   + 
* (myapi) ubuntu@jumpto:/etc/nginx/sites-available$ sudo nano myapi

```
    server {
            listen 80;
            server_name 고정IP;
    
            location = /favicon.ico { access_log off; log_not_found off; }
    
            location / {
                    include proxy_params;
                    proxy_pass http://unix:/tmp/myapi.sock;
            }
    }
```
```commandline
    위의 Nginx 설정은  nginx를 80번 포트에 바인딩하고, 
    고정IP 도메인 이름을 사용합니다. 
    nginx는 80번 포트로 들어오는 웹 요청을 127.0.0.1의 8000번 포트로 전달합니다. 
    즉, nginx는 80번 포트로 들어오는 웹 요청을 
    포트 번호 8000을 사용하는 gunicorn에 전달합니다.
    gunicorn은 파이썬 웹 애플리케이션을 실행하는 웹 서버입니다.

    
    location / { ... }은 
    / URL로 시작하는 모든 요청을 Gunicorn 소켓이 처리하게 한다.
```

* 방금 작성한 Nginx 를 설정한 myapi 파일을 Nginx가 환경 파일로 읽을 수 있도록 설정해야 한다. 
   + cd /etc/nginx/sites-enabled/
   + (myapi) ubuntu@tutorial:/etc/nginx/sites-enabled$ sudo rm default
   + (myapi) ubuntu@tutorial:/etc/nginx/sites-enabled$ sudo ln -s /etc/nginx/sites-available/myapi

##### Nginx 실행  
* (myapi) ubuntu@tutorial:/etc/nginx/sites-enabled$ sudo systemctl restart nginx
   + Nginx 설정을 적용하려면 Nginx를 재 시작해야 한다.


### [4-11 서버에 로깅 적용하기](https://wikidocs.net/177312)
#### at AWS Lightsail  
##### Gunicorn 서비스 파일 수정하기
* (myapi) ubuntu@tutorial:/etc/systemd/system$ sudo nano myapi.service
   + 아래와 같이 --log-config 옵션을 추가하고   
     --log-config 옵션에 추가한 uvicorn_log.ini 파일을 생성하면   
     Gunicorn의 로그를 출력할수 있다.
```
    [Unit]
    Description=gunicorn daemon
    After=network.target
    
    [Service]
    User=ubuntu
    Group=ubuntu
    WorkingDirectory=/home/ubuntu/projects/myapi
    ExecStart=/home/ubuntu/.local/bin/gunicorn \
              main:app \
              --workers 2 \
              --worker-class uvicorn.workers.UvicornWorker \
              --bind unix:/tmp/myapi.sock \
              --log-config /home/ubuntu/projects/myapi/logs/uvicorn_log.ini
    [Install]
    WantedBy=multi-user.target
```

#### Gunicorn 로깅 설정 파일 만들기
* /home/ubuntu/projects/myapi/logs/uvicorn_log.ini 파일을 생성합니다.
```
[loggers]
keys=root

[handlers]
keys=logfile

[formatters]
keys=logfileformatter

[logger_root]
level=DEBUG
handlers=logfile

[formatter_logfileformatter]
format=[%(asctime)s.%(msecs)03d] %(levelname)s [%(thread)d] - %(message)s

[handler_logfile]
class=handlers.RotatingFileHandler
level=DEBUG
args=('logs/myapi.log','a')
formatter=logfileformatter
```
   + logs 디렉터리에 myapi.log 라는 이름의 로그파일을 생성하게 했고 
   + 로그레벨은 DEBUG로 설정했다.
   + 운영 환경에서는 DEBUG 대신 INFO 또는 ERROR로 설정하기를 추천한다.

#### 서버 로그 확인하기

* 위와 같이 설정을 마치고 Gunicorn 서비스를 재시작합니다.
   + ~~(myapi) ubuntu@tutorial:/etc/nginx/sites-enabled$ sudo systemctl restart nginx~~
   + (myapi) ubuntu@tutorial:/etc/nginx/sites-enabled$ sudo systemctl restart myapi.service    
    
* (myapi) ubuntu@jumpto:~/projects/myapi/logs$ tail -f myapi.log  


#### Nginx 로그 설정하기  
* (myapi) ubuntu@tutorial:/etc/nginx/sites-available$ sudo nano myapi
```
server {
        listen 80;
        server_name 52.2.184.246;

        location = /favicon.ico { access_log off; log_not_found off; }

        location / {
                access_log /home/ubuntu/projects/myapi/logs/nginx_access.log;
                error_log  /home/ubuntu/projects/myapi/logs/nginx_error.log;

                include proxy_params;
                proxy_pass http://unix:/tmp/myapi.sock;
        }
}
```
* 위와 같이 /etc/nginx/sites-available/myapi 에 Nginx 설정을 추가한 후,  
  Nginx를 재시작하면 로그가 출력됩니다.
   + (myapi) ubuntu@tutorial:/etc/nginx/sites-enabled$ sudo systemctl restart nginx
