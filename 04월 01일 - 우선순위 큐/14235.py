# 파이썬은 최소 힙이 기본이므로 - 붙여서 넣고 - 붙여서 빼기  

import heapq
presents=[]
heapq.heapify(presents)

n=int(input())
for i in range(n):
    temp=list(map(int,input().split()))
    if temp[0]==0:
        if len(presents)>0:
            print(heapq.heappop(presents)*(-1))
        else:
            print(-1)
    else:
        for j in range(1,len(temp)):
            heapq.heappush(presents,temp[j]*(-1))
            
        
