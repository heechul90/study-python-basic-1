### Unit 31. 함수에서 재귀호출 사용하기
## 31.5 심사문제: 재귀호출로 피보나치 수 구하기
## 표준 입력으로 정수 한 개가 입력됩니다(입력 값의 범위는 10~30).
## 다음 소스 코드를 완성하여 입력된 정수에 해당하는 피보나치 수가 출력되게 만드세요.

## 피보나치 수는 0과 1로 시작하며,
## 다음 번 피보나치 수는 바로 앞의 두 피보나치 수의 합입니다.

# n
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21...

# 결과
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946...

# 입력
# 10
# 결과
# 55

# 입력
# 20
# 결과
# 6765

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))



