# 파이썬을 이용하여 웹서비스를 개발하는 기술 습득
    # 모델(머신러닝/딥러닝등으로 학습한 결과물)을 동일한 언어로 서비스하기 위해
    # 파이썬으로 웹서비스 구성법을 익힌다(단, 웹서비스시)
    # flask를 이용하여 간단한 웹페이지 구성 및 구성요소 이해

# 0단계 필요모듈설치
'''
    # $ pip install flask
    # $ conda install flask
'''

# TODO 1단계 모듈가져오기
from flask import Flask

# TODO 2단계 Flask 객체 생성
app = Flask(__name__)

# TODO 3단계 라우팅:URL을 정의, 
    # 특정 URL 요청시 처리하는(요청을 처리,응답을 구성, 실제 응답수행 모든 행위)
    # 함수를 정의하여 매칭한다
    # 고유한 url 1개와 함수 1개를 매칭한다
    # ->전제       : 웹서비스, 기획서상의 스토리보드 존재가필요
    # ->프로토콜표 : 미들웨어 서비스, 화면이 없는 웹서비스, 통신만 수행함
    #                이런 경우 웹의 화면, 서비스는 전부 클라이언트가 담당한다
    #               ex) reactjs, angular, vue => js or 타입스크립트로 클라이언트개발
    # @:데코레이터 -> 자바에서는 어노테이션이라고 부름
@app.route('/')
def home():
    # 함수 내부는 현재로써는 문자열을 리턴해야 한다!! 이것만 유지
    return 'home page'

# URL 추가 가능, 함수명은 다르게 해야함
@app.route('/login')
def login():
    # 함수 내부는 현재로써는 문자열을 리턴해야 한다!! 이것만 유지
    return 'Login page'

# url 경로는 /구분자를 통해서 depth를 깊게 줄수 있다
# ~/users/login
@app.route('/users/login')
def user():    
    return 'user/login page'

# TODO 4단계 서버 가동 -> 엔트리 포인트 지정, 시작점 설정
if __name__ == '__main__':
    # 서버 가동
    app.run()
