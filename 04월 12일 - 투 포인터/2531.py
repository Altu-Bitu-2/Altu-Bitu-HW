# 슬라이딩 윈도우

import sys
input=sys.stdin.readline

from collections import defaultdict

n,d,k,c=map(int,input().split())
sushi=[]
for i in range(n):
    sushi.append(int(input()))
sushi.extend(sushi) # 원형이어서 배열 2개 붙임 

dict_=defaultdict(int)
dict_[c]+=1

answer=0

left=0
right=0

while right<k:
    dict_[sushi[right]]+=1
    right+=1

while right<len(sushi): 
    dict_[sushi[left]]-=1
    if dict_[sushi[left]]==0: # 0이라고 자동으로 지워지지 않음 
        del dict_[sushi[left]]
    dict_[sushi[right]]+=1
    answer=max(answer,len(dict_))
    left+=1
    right+=1

print(answer)
