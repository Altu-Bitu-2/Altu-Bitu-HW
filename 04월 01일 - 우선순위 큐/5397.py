# 1. 커서 위치 직접 이동시키면서 문자열 구하는 경우 -> 시간 초과
# 2. 커서는 고정하고 커서 위치 기준으로 left, right 배열 만들기.  

import sys
input=sys.stdin.readline

n=int(input())

def checkPw(pw):
    tmp=[]
    left=[]
    right=[]
    
    for i in range(len(pw)):
        if pw[i].isalpha() or pw[i].isdigit():
            left.append(pw[i])
        elif pw[i]=="<":
            if len(left)>0:
                right.append(left.pop())
        elif pw[i]==">":
            if len(right)>0:
                left.append(right.pop())
        elif pw[i]=="-":
            if len(left)>0:
                left.pop()

    left.extend(reversed(right)) # ★

    return ''.join(left)
    

for i in range(n):
    pw=input()
    print(checkPw(pw))
