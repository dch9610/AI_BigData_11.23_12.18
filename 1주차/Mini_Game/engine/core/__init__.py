from engine import *

# TODO 함수지향적 프로그램 STEP1
def game_step1():
    # print("game_step1 call")
    game_start_prompt = 'Enjoy Custom Game World'
    print( game_start_prompt )
    pass

# TODO 함수지향적 프로그램 STEP2
'''
    - "게임 제목을 입력하세요, 단 20자 이내로 입력 가능합니다." 
    라는 문구가 출력된다
    - 플레이어가 입력할때까지 무제한으로 대기한다
    - 아무것도 입력하지 않고 엔터를 치면(조건1) "정확하게 입력하세요" 라고 출력하고 
    다시 입력 대기한다
    - 20자 이상 입력하고 엔터를 치면(조건2), "20자가 초과되었습니다." 라고 출력하고,
    다시 입력 대기한다.
    - 20자 이내로 입력하고 엔터를 치면(조건3) gameTitle이라는 변수에 게임 제목을
    담고 다음 단계로 이동한다 -> 반복문을 빠져나간다
'''
def game_step2():
    gameTitle = None
    msg = f"게임 제목을 입력하세요, 단 {ENV_TITLE_MAX_LEN}자 이내로 입력 가능합니다.: "
    while True:
        gameTitle = input(msg).strip()
        if not gameTitle:
            print("정확하게 입력하세요")
            continue      
        elif len(gameTitle) > ENV_TITLE_MAX_LEN:
            print(str(ENV_TITLE_MAX_LEN) + "자가 초과되었습니다.")
            continue
        break
    # 함수 내부에서 세팅된 게임 제목은 다른 함수에서 사용하므로
    # 리턴해줘야 한다. (함수 밖으로)
    return gameTitle 


# TODO 함수지형적 프로그램 STEP3
'''
    - 플레이어의 닉네임을 입력하시오, 단 15자로 제한한다"
    - 입력에 대한 체크 포인트는 Step2와 동일하다
    - 플레이어에 대한 닉네임은 player_name이라는 변수에 보관한다
'''
def game_step3():
    player_name = None
    msg         = "플레이어의 닉네임을 입력하시오, 단 %s자로 제한한다: "  % ENV_PNAME_MAX_LEN
    while not player_name:
        tmp         = input(msg).strip()
        if not tmp:
            print('정확하게 입력하세요')
            pass
        elif len(tmp) > ENV_PNAME_MAX_LEN:
            print( '닉네임은 {}자 이내로 입력하세요'.format(ENV_PNAME_MAX_LEN) )
            pass
        else:
            player_name = tmp
            break
    return player_name


# TODO 함수지형적 프로그램 STEP4
'''
    ------------------------------
    -         게임 제목          -
    -          v 1.0             -
    -   welcome 플레어이름       - 
    ------------------------------
'''
def game_step4(gameTitle, player_name):
    
    p_max_len = 2 + 2 + 1 + len('welcome') + ENV_PNAME_MAX_LEN
    print( '-'*p_max_len )
    print(f'-{gameTitle:^25}-')
    print(f'-{VERSION:^25}-')
    print(f'-{"welcome "+player_name:^25}-')
    print( '-'*p_max_len )
    print('\n 게임이 시작됩니다. AI가 숫자를 준비합니다. \n')
    pass

# TODO 함수지형적 프로그램 STEP5
'''
  - AI가 1 ~ 100 사이의 임의의 수를 정수로 하나 **랜덤**하게
  생성한다.
  - "1<= x <=100에서 값을 하나 선택하세요"
  - 사용자는 1 ~ 100 사이에 값을 입력한다.
  - 입력을 안하고 Enter
  - 1보다 작거나, 100보다 큰값을 넣고 Enter
  - 숫자가 될수 없는 값을 넣고 Enter
  - 정상적인 값을 입력하고 Enter
'''

def game_step5(msg):
    guest_number = None
    while True: 
      guest_number = input(msg).strip()

      if not guest_number:
        print("정확하게 입력하세요")
        continue

      if not guest_number.isnumeric():
        print("{0}는 숫자가 아니거나, 대상이 아닙니다.".format(guest_number))
        continue

      guest_number = int(guest_number)
      if guest_number < 1 or guest_number > 100:
        print("허용하는 값의 범위를 넘어갔습니다.")
        continue
      break
    return guest_number

# TODO 함수지형적 프로그램 STEP6
'''
      - 판정 : 작으면 작다. 크면 크다라고 출력하고 다시 입력 대기를 한다
      - 만약, 정답을 맞추면 총 시도횟수를 10에서 빼서 10을 곱한다. 이것을 이번 판의 획득 점수로 표현한다.
      - "총 5회 시도해서 50점을 획득하였습니다. 다시하시겠습니까?"
        - yes : 다시 게임시작
        - no : 게임종료
      - 게임종료 : good bye~
'''
def game_step6(tryCnt,ai_number, guest_number):
    isSuccess = False
    play_game = True
    if ai_number > guest_number:
        print("크다")
    elif ai_number < guest_number:
      print("작다")
    else:
      isSuccess = True

    # 정답을 맞춘 경우 점수 산정
    if isSuccess:
      point = (10 - tryCnt) * 10
      if point < 0:
        point =0
      print(f"총 {tryCnt}회 시도해서 {point}점을 획득하였습니다. 다시하시겠습니까?: ")

      # 재시작 여부 물어보기
      while True:
        choice = input("yes : 다시게임시작, no : 게임종료: ").strip().lower()
        if choice == 'yes' or choice == 'y':
          break
        elif choice == 'no' or choice == 'n':
          play_game = False
          break
        else:
          print("정확하게 입력하세요")
    return isSuccess, play_game