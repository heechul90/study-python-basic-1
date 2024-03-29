### Unit 23. 2차원 리스트 사용하기
## 23.2 반복문으로 2차원 리스트의 요소를 모두 출력하기

a = [[10, 20], [30, 40], [50, 60]]

for x, y in a:       # 리스트의 가로 한 줄(안쪽 리스트)에서 요소 두 개를 꺼냄
    print(x, y)


## 23.2.2  for 반복문을 두 번 사용하기
a = [[10, 20], [30, 40], [50, 60]]

for i in a:        # a에서 안쪽 리스트를 꺼냄
    for k in i:    # 안쪽 리스트에서 요소를 하나씩 꺼냄
        print(k, end=' ')
    print()


## 23.2.3  for와 range 사용하기
a = [[10, 20], [30, 40], [50, 60]]

for i in range(len(a)):            # 세로 크기
    for k in range(len(a[i])):     # 가로 크기
        print(a[i][k], end = ' ')
    print()


## 23.2.4  while 반복문을 한 번 사용하기
a = [[10, 20], [30, 40], [50, 60]]

i = 0
while i < len(a):    # 반복할 때 리스트의 크기 활용(세로 크기)
    x, y = a[i]      # 요소 두 개를 한꺼번에 가져오기
    print(x, y)
    i += 1           # 인덱스를 1 증가시킴


## 23.2.5  while 반복문을 두 번 사용하기
a = [[10, 20], [30, 40], [50, 60]]

i = 0
while i < len(a):           # 세로 크기
    j = 0
    while j < len(a[i]):    # 가로 크기
        print(a[i][j], end=' ')
        j += 1              # 가로 인덱스를 1 증가시킴
    print()
    i += 1                  # 세로 인덱스를 1 증가시킴


