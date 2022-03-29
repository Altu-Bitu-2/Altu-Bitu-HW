# 메모리 초과 해결 위해서는 True, False로 저장해주는 아이디어 말고도
# 코드 효율적으로도 수정해야 함 (https://www.acmicpc.net/submit/11723/41132196)

# 더 빨리 input 받기 
import sys
input=sys.stdin.readline

n=int(input())

check=[False]*20 # 있으면 True, 없으면 False

for i in range(n):
    operation=input()
    
    a=(operation.split())[0] # 수행해야 할 연산의 종류
    
    if a=="all":
        check=[True]*20
        continue
    
    elif a=="empty":
        check=[False]*20
        continue
        
    b=(operation.split())[1] # x -> str로 받아진 것 주의! 

    if a=="add":
        check[int(b)-1]=True

    elif a=="remove":
        check[int(b)-1]=False
        
    elif a=="check":
        if check[int(b)-1]==True:
            print(1)
        else:
            print(0)

    elif a=="toggle":
        if check[int(b)-1]==True:
            check[int(b)-1]=False
        else:
            check[int(b)-1]=True
