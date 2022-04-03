# 백트래킹 정말 어렵다!! 트리처럼 해보면 조금 이해됨 
# 참고: https://codinghani.tistory.com/51?category=960304

# 재귀 깊이 깊어지면
# import sys
# sys.setrecursionlimit(10**6)

import sys
input=sys.stdin.readline

n,m=map(int,input().split())

l=list(map(int, input().split()))
l.sort()

check=[False]*n # 10000이 아니라 n으로
temp=[0]*m # 한 줄마다 임시로 저장할 리스트 

def backtracking(now):
    if now==m: # 탈출 조건을 n이라고 생각했는데 m이었음 
        for i in range(m):
            print(temp[i], end=" ")
        print()
        return
    t=0 # 같은지 비교하려고
    for i in range(n): # [1,7,9,9]에서 1에서 시작하는지, 7에서 시작하는지, 9에서 시작하는지, 9에서 시작하는지
        if check[i] or t==l[i]:
            continue
        check[i]=True
        temp[now]=l[i]
        backtracking(now+1)
        check[i]=False
        t=temp[now]
    
backtracking(0)
