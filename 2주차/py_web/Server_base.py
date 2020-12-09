# 기본 템플릿
# TODO 1단계 모듈가져오기
from flask import Flask

# TODO 2단계 Flask 객체 생성
app = Flask(__name__)

# TODO 3단계 라우팅:URL을 정의
@app.route('/')
def home():    
    return 'home page2'

# TODO 4단계 서버 가동 -> 엔트리 포인트 지정, 시작점 설정
if __name__ == '__main__':    
    app.run(debug=True)