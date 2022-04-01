# 추가제출

# 빠르게 입력
import sys
sys.stdin.readline

"""
[연산자 끼워넣기]
연산자를 모두 돌려보면서 배치한 후, 각 연산자에 따른 값 계산
"""

MAX = 10**9 # 문제에서 최대 10억이라 했음 

add = lambda x, y: x + y # 더하는 함수 
sub = lambda x, y: x - y # 빼는 함수 
multiply = lambda x, y: x * y # 곱하는 함수 

# C++14 방식에 맞추어 나누기 함수 작성
def division(x, y):
    if x < 0: # 음수일 때
        return - (-x // y) # -x로 양수로 만들고 몫을 다시 음수로 만든다
    return x // y # 양수일 때 

# 인덱스에 맞는 연산을 하기 위해 함수를 리스트에 저장
functions = [add, sub, multiply, division]

# cnt: 수 인덱스, value: 현재까지 연산 결과
def backtracking(cnt, value):
    global max_value, min_value # 전역 변수로 
    if cnt == n:    # 연산이 모두 완료 되었다면
        max_value = max(max_value, value) # 둘 중 큰 값
        min_value = min(min_value, value) # 둘 중 작은 값 
        return

    for i in range(4): # functions의 갯수가 4니까 
        if operator[i] > 0: # 덧셈/뺄셈/곱셈/나눗셈의 개수가 0보다 클 때 
            operator[i] -= 1 # 한 번 쓰니까 빼주고 
            backtracking(cnt + 1, functions[i](value, numbers[cnt]))    # i번째 함수에 value와 numbers[cnt]를 인자로 넘겨주어 계산함
            operator[i] += 1 # 다음 탐색을 위해 다시 더해줌 
    return

# 입력
n = int(input()) # numbers에서 받을 수의 개수 
numbers = list(map(int, input().split())) # 주어진 수들 
operator = list(map(int, input().split())) # 연산자 별 개수 

max_value = -MAX   # 현재까지 최대값 기록
min_value = MAX    # 현재까지 최솟값 기록

# 연산
backtracking(1, numbers[0])
# 출력
print(max_value, min_value, sep='\n')
