# 함수 지향적 프로그램으로 숫자 맞추기 게임 진행
# 파이썬 자체, 서드 파트 모듈
import random

# 내가 만든 모듈
# from engine.core import game_step1, game_step2, game_step3
from engine.core import *
'''
    # 엔트리포인트 (프로그램의 시작점, 진입로) 필요 -> main 통상
    # 통상적으로 인자값을 프로그램 구동시 받게 하여 게임 컨트롤을 할 수 있게 한다.
    # : 딥러닝시 실험 환경을 부여하는 것과 동일
    # 여기서는 생략
'''
def main():
    game_step1() # STEP1() 호출
    gameTitle = game_step2() # STEP2() 호출 ,game_step2의 리턴값을 변수에 저장
    print( '게임 제목은: ', gameTitle )
    player_name = game_step3() # STEP3() 호출
    print('플레이어의 닉네임: ', player_name)
    game_step4(gameTitle, player_name) # STEP4() 호출, 인자를 활용하여 
    play()
    pass

def play():
    msg = "1 <= x <= 100에서 값을 하나 선택하세요: "
    play_game = True # 재시작 여부

    while play_game: # 전체 게임의 진행 여부
        tryCnt = 0
        ai_number = random.randint(1,100)
        isSuccess = False
        while not isSuccess: # 게임 1판에 대한 진행여부
            guest_number = game_step5(msg) # STEP5() 호출
            tryCnt += 1
            isSuccess, play_game = game_step6(tryCnt,ai_number, guest_number) # STEP6() 호출
            pass
    print("good bye~!!")
    pass

# 엔트리포인트 지정
if __name__ == '__main__':
    print("프로그램 시작")
    main()
