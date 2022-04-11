import sys
input=sys.stdin.readline

n,m=map(int, input().split())

# Q. 행렬을 받을 때 list(map(int, input().split())) 하면 0000 -> 0으로 합쳐져 버려서
# 이렇게 받았는데 더 나은 방법이 있나요? 그리고 원래 input 받으면 계속 \n이 뒤에 붙는 건가요? 
a=[list(map(int, list(input())[:-1])) for _ in range(n)]
b=[list(map(int, list(input())[:-1])) for _ in range(n)]

answer=0

def changeArray(a, x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            if a[i][j]==1:
                a[i][j]=0
            else:
                a[i][j]=1

def checkArray(a, b):
    flag=1
    for i in range(n):
        for j in range(m):
            if a[i][j]!=b[i][j]:
                flag=0
                break
    return flag

for i in range(n-2): 
    for j in range(m-2): 
        if a[i][j]!=b[i][j]: # 그리디로, 최솟값으로 만들어주는 부분
            changeArray(a,i,j)
            answer+=1

if checkArray(a,b)==1:
    print(answer)
else:
    print(-1)
