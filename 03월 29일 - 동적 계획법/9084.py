import sys
input = sys.stdin.readline

"""
 dp[i] = 주어진 동전 종류를 사용해서 i원을 만드는 경우의 수
 dp[0] = 1 을 넣고 시작 (0원을 만드는 경우의 수 1로 생각)
 각 동전마다 해당 동전부터 만들어야 하는 금액(m)까지 돌리면서 해당 동전을 사용하기 전 금액의 경우의 수와 현재 경우의 수를 더함
 !주의! 이때, 해당 동전 사용하기 전 금액의 경우의 수가 0이면 금액을 만들 수 없는 경우이므로 더하면 안됨
"""

MAX = 10**4 # 주어진 금액의 최댓값 

def count(n, m, coin):
    dp = [0] * (m+1) # 주어진 금액까지 저장할 수 있는 배열 생성 
    dp[0] = 1 # 0원을 만드는 경우의 수 1로 생각 

    for c in coin: # 각 동전을 순회하면서 
        for idx in range(c, m+1): # 목표 금액까지 
            dp[idx] += dp[idx - c] # 동전 사용하기 전 금액에서의 경우의 수를 더함 

    return dp[m] # 주어진 금액의 경우의 수 리턴 

# 입력
t = int(input()) # 테스트 케이스 개수

for _ in range(t):
    # 입력
    n = int(input()) # 동전 개수 
    coin = list(map(int, input().split())) # 동전의 종류 배열로 저장 
    m = int(input()) # 목표 금액 
    # 연산 + 출력
    print(count(n, m, coin))
