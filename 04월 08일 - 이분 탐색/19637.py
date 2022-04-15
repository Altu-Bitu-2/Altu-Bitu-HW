import sys
input=sys.stdin.readline
from bisect import bisect_left

n,m=map(int,input().split())
system=[input().split() for _ in range(n)]

name=[]
value=[]

for s in system:
    name.append(s[0])
    value.append(int(s[1]))

arr=[int(input()) for _ in range(m)]
        
for a in arr:
    idx=bisect_left(value,a)
    print(name[idx])
