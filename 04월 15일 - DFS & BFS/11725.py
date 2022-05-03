import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

n=int(input())

adj_list=[[] for _ in range(n+1)]
parents=[0]*n

for i in range(n-1):
    a,b=map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)


def dfs(x):
    for i in adj_list[x]:
        if i==1:
            continue
        if parents[i-1]==0:
            parents[i-1]=x
            dfs(i)

dfs(1)

for i in range(1,n):
    print(parents[i])
