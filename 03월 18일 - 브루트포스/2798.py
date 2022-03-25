import sys
from itertools import combinations
input = sys.stdin.readline

"""
[ 블랙잭 ] - 단순 구현
카드가 최대 100장이므로,
C(100, 3) < 100*100*100 = 1,000,000 -> 브루트포스 충분히 가능
ver1. 3중 for문 이용해서 구현
+) 코드의 효율성을 높이기 위해, 카드를 사전에 정렬하여 M을 넘어가는 순간 반복 종료
ver2. itertools.combinations 이용하여 모든 조합을 구해서 구현
"""

def play_blackjack(n, m, cards):
    cards.sort()    # 오름차순 정렬
    answer = 0 # 값 더해주기 위해 0으로 초기화 

    # 3개짜리 조합을 3중 for문으로 구현함 
    for i in range(n):
        for j in range(i+1, n): # i와 겹치지 않도록 i+1부터
            for k in range(j+1, n): # j와 겹치지 않도록 j+1부터 
                temp = cards[i] + cards[j] + cards[k] # 3장의 합 
                # cards 리스트가 오름차순 정렬되어 있으므로 k를 키우는 건 의미 없음
                if (temp > m): # M을 넘으면 안 됨 
                    break # 반복문 탈출 
                answer = max(answer, temp)  # 최댓값 갱신
    return answer # M을 넘지 않는 최댓값 return 

def play_blackjack_with_combinations(n, m, cards):
    combi = combinations(cards, 3)   # cards에서 3개로 이루어진 모든 조합 구하기
    arr = list(map(lambda x:sum(x), combi)) # 모든 조합에 대해 합 구하기
    arr.sort()  # 오름차순 정렬

    answer = 0 # 값 더해주기 위해 0으로 초기화
    for total in arr: # 모든 조합 순회 
        # 합이 m을 넘어가면 바로 종료
        if total > m:
            break # 반복문 탈출
        answer = total # 이 코드에 도착한 것은 합이 m을 넘어가지 않았다는 뜻이고 이미 오름차순 정렬되었으므로 
    
    return answer # M을 넘지 않는 최댓값 return 


# 입력
n, m = map(int, input().split())
cards = list(map(int, input().split()))

# play_blackjack, play_blackjack_with_combinations 둘 다 OK 
print(play_blackjack(n, m, cards)) 
# print(play_blackjack_with_combinations(n, m, cards))
