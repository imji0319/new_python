
# 해당 파일의 인코딩 선언
# -*- coding: utf-8 -*-

from flask import Flask

# Flask 애플리케이션을 만들려면 Flask 객체를 생성해야 함.
app = Flask(__name__)

# route() 데코레이터를 사용 , 루트 경로(/)를 호출했을 때 hello_flask() 함수가 실행
# URL을 처리하는 기능을 만들 수 있음 
@app.route('/')

def hello_flask():
    return "Hello Flask"

if __name__ == '__main__':
    app.run()