# 클라이언트가 특정 페이지를 요청할때, 데이터를 서버로 보낼수 있다
    # case 1 : method를 이용하여 전송, GET, POST, PUT, DELETE,...
    #          http 프로토콜을 이용하여 데이터를 전송
    #          메소드에 따라 목적과 방식, 스타일, 화면반응이 다르다
    #          GET, POST에 집중하여 작업
    # case 2 : url에 싣어서 전송 -> 동적파라미터(크기제한은 있음)
    # <동적파라미터>
    # 장점 : 빠르게 서버쪽으로 데이터전송하는 시스템구축->프로토타입에 유리
    #        URL의 무한 확장 가능

# TODO 1단계 모듈가져오기
# html로 응답하기->랜더링
from flask import Flask,render_template

# TODO 2단계 Flask 객체 생성
app = Flask(__name__)

# TODO 3단계 라우팅:URL을 정의, 

@app.route('/')
def home():
    # 함수 내부는 현재로써는 문자열을 리턴해야 한다!! 이것만 유지
    return 'home page'

@app.route('/html')
def html(): 
    # 여기서 html을 보내주는것은 맞으나, 그 긴 코드들을 문자열로 굳이 만들어서
        # 보내는것은 적합하지 않다 -> 구조적, 유지보수적, 확장성 적으로 다부적절   
        # -> render_template() 함수를 이용하여 처리
        # 엔트피 포인트에 templates하는 폴더를 만들고(현재는 이름 고정)
        # 그 밑에 html 파일을 두고, 참조하여 처리한다
    return '''
        <h1>html 직접 표현</h1>
    '''


# 동적 파라미터 case 1 - 기본형
    # 기자기 뉴스를 입력하면 고유 아이디를 부여하여 관리한다
    # 뉴스의 고유 아이디는 공개되도 상관없다
    # http://127.0.0.1:5000/news/%EA%B0%801aA!
    # 한글,영대,영소,숫자, 특수문자 이상없음 
    # 한글을 코드에 붙이면 > %EA%B0%80 이렇게 보인다(인코딩문자)
    # 한글이 그냥 가면 깨지기 때문에 자동처리가 되었다(필요하면 수동처리함)
@app.route('/news/<news_id>')
def news(news_id):    
    # 함수 외부에서 함수 내부로 데이터를 전달하고 싶으면, 인자를 통해서 전달
    return '뉴스 %s' % news_id
    #return '뉴스 ' + news_id

@app.route('/show')
def show(): 
    # HTML을 수정한다고 해서 서버가 재가동되지 않는다
    # html은 반드시 templates 폴더 이하에 파일로 저장하여 관리한다
    return render_template('index.html')

# TODO 4단계 서버 가동 -> 엔트리 포인트 지정, 시작점 설정
if __name__ == '__main__':
    # 서버 가동
    app.run()
