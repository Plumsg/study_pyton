
# 점수계산 = 과목점수/m*100

#과목수 n입력받기
n = int(input())
#각 과목의 점수를 담을 리스트 만들기
grade =list(map(int, input().split()))
# m = 점수의 최대값
m = max(grade)
a = 0
# for문을 활용해서 각 점수 하나씩 보기
for i in grade:
    a+= i / m*100 # 각 과목의 새로운 점수
    
# 평균 = 점수의 합 / 과목 수 n
print(a/n)
# 최종값 = 평균 (intX)