### Unit 19. 계단식으로 별 출력하기
## 19.3 계단식으로 별 출력하기

for i in range(5):              # 0부터 4까지 5번 반복. 세로 방향
    for j in range(5):          # 0부터 4까지 5번 반복. 가로 방향
        if j <= i:              # 세로 방향 변수 i만큼
            print('*', end='')  # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
    print()                     # 가로 방향으로 별을 다 그린 뒤 다음 줄로 넘어감
                                # (print는 출력 후 기본적으로 다음 줄로 넘어감)




## 19.3.1  대각선으로 별 출력하기
for i in range(5):
    for k in range(5):
        if i == k:
            print('*', end = '')
        if i > k:
            print(' ', end = '')   
    print()


for i in range(5):              # 0부터 4까지 5번 반복. 세로 방향
    for j in range(5):          # 0부터 4까지 5번 반복. 가로 방향
        if j == i:              # 세로 방향 변수와 같을 때
            print('*', end='')  # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
        else:                   # 세로 방향 변수와 다를 때
            print(' ', end='')  # 공백 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
    print()                     # 가로 방향으로 별을 다 그린 뒤 다음 줄로 넘어감
                                # (print는 출력 후 기본적으로 다음 줄로 넘어감)

            