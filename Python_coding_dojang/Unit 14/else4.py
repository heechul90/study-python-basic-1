### Unit 14. else를 사용하여 두 방향으로 분기하기
## 14.4 조건식을 여러 개 지정하기
x = 10
y = 20
 
if x == 10 and y == 20:     # x가 10이면서 y가 20일 때
    print('참')
else:
    print('거짓')



## 14.4.1  중첩 if 조건문과 논리 연산자
if x > 0:
    if x < 20:
        print('20보다 작은 양수입니다.')

if x > 0 and x < 20:
    print('20보다 작은 양수입니다.')

if 0 < x < 20:
    print('20보다 작은 양수입니다.')


