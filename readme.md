# todolist
Wintercoding 과제: todo list✍ 만들기  
https://wintercoding-todolist.herokuapp.com/


## 설치 순서
    # PostgreSQL 설치 및 DB 생성
    sudo apt-get install postgresql
    
    sudo -u postgres psql
    CREATE USER admin with password '1234';
    CREATE DATABASE todolist OWNER admin;
    
    # 가상환경 설치 및 실행
    pip install virtualenv
    virtualenv env/todolist
    source env/todolist/bin/activate
    
    git clone git@github.com:jmpark6846/todolist.git
    cd todolist    
    
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
    
## 개발/배포 환경
- Python 3.6.6
- Django 2.12
- PostgreSQL 10.5
- Ubuntu 18.04
- jQuery 3.3.1
- jQuery UI 1.12.1
- Bootstrap 4.1.3 
- heroku
