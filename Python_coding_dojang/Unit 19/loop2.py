### Unit 19. 계단식으로 별 출력하기
## 19.2 사각형으로 별 출력하기

for i in range(5):          # 5번 반복. 바깥쪽 루프는 세로 방향
    for j in range(5):      # 5번 반복. 안쪽 루프는 가로 방향
        print('*', end='')  # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
    print()                 # 가로 방향으로 별을 다 그린 뒤 다음 줄로 넘어감
                            # (print는 출력 후 기본적으로 다음 줄로 넘어감)



## 19.2.1  사각형 모양 바꾸기

for i in range(3):          # 3번 반복. 세로 방향
    for j in range(7):      # 7번 반복. 가로 방향
        print('*', end='')  # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
    print()                 # 가로 방향으로 별을 다 그린 뒤 다음 줄로 넘어감
                            # (print는 출력 후 기본적으로 다음 줄로 넘어감)