import random

# 정답 숫자 생성
def generate_answer():
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:3]

# 스트라이크와 볼 개수 계산
def calculate_score(answer, guess):
    strike = 0
    ball = 0
    for i in range(len(answer)):
        if answer[i] == guess[i]:
            strike += 1
        elif guess[i] in answer:
            ball += 1
    return strike, ball

# 게임 시작
def start_game():
    answer = generate_answer()
    print("숫자 야구 게임을 시작합니다!")
    while True:
        # 사용자 입력 받기
        guess = input("숫자 3개를 입력하세요 (예: 123): ")
        if len(guess) != 3 or not guess.isdigit():
            print("잘못된 입력입니다. 다시 시도하세요.")
            continue

        # 스트라이크와 볼 개수 계산
        strike, ball = calculate_score(answer, list(map(int, guess)))

        # 결과 출력
        if strike == 3:
            print("정답입니다!")
            break
        else:
            print(f"{strike}S {ball}B 입니다. 다시 시도하세요.")

# 게임 실행
start_game()