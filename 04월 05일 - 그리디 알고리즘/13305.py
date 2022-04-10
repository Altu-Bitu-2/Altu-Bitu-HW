import sys
input=sys.stdin.readline

n=int(input()) 
distance=list(map(int, input().split())) 
price=list(map(int, input().split())) 

# 리터당 가격 쭉 순회하면서 5 -> 2 -> 4 -> .. 자기보다 작으면 바꿔주기  

answer=0

price=price[:-1] # 마지막 가격은 어차피 상관 없어서 삭제

now=price[0] 
answer+=distance[0]*now

for i in range(1,len(price)): 
    if price[i]<now:
        now=price[i]
    answer+=distance[i]*now
    
print(answer)


'''
# 처음에 시도했던 풀이

dp=[0]*(n-1) # 각 도시에서의 최소 비용 저장 

for i in range(1,n): 
    if i==1:
        dp[i-1]=price[i-1]*distance[i-1]
    else: # 리터당 가격의 최소가 바로 전보다 앞에 있을 수도 있어서 틀림!! 
        dp[i-1]=dp[i-2]+min(price[i-1],price[i-2])*distance[i-1]

print(dp[-1])
'''
