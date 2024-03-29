### Unit 8. 불과 비교, 논리 연산자 알아보기
## 8.4 연습문제: 합격 여부 출력하기

# 국어, 영어, 수학, 과학 점수가 있을 때 한 과목이라도 50점 미만이면 불합격
korean = 92
english = 47
mathematics = 86
science = 81

print(korean > 50 and english > 50 and mathematics > 50 and science > 81)



### Unit 8. 불과 비교, 논리 연산자 알아보기
## 8-5 심사문제 : 합격 여부 출력하기

# 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
# 국어는 90점 이상, 영어는 80점 초과, 수학은 85점 초과, 과학은 80점 이상일 때 합격이라고 정했습니다.
# (한 과목이라도 조건에 만족하지 않으면 불합격).
# 다음 소스 코드를 완성하여 합격이면 True,
# 불합격이면 False가 출력되게 만드세요.
# (input에서 안내 문자열은 출력하지 않아야 합니다)

a, b, c, d = map(int, input().split())
print(a >= 90 and b > 80 and c > 85 and d >= 80)