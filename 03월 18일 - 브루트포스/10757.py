# A,B = map(int, input().split())
# print(A+B)
# 이렇게 하면 일단 통과! 

A,B = map(str, input().split())

if len(B)>len(A): # 항상 A가 더 길게
    A, B = B, A
    # p2. 파이썬은 swap할 때 중간 임시변수 필요 없음! 
    #swap=A
    #A=B
    #B=swap
    
a_length = len(A)
b_length = len(B)

stack=[]

answer=""

add=0 # 덧셈할 때 10 넘어서 윗 열에서 더해줘야 하는 수

if a_length==b_length: # A와 B의 길이가 같을 때 
    for i in range(a_length):
        tmp=int(A[-1-i])+int(B[-1-i])
        tmp+=add # 지난 열에서 10 넘어서 더해줘야 하는 수 더하기 
        add=0 # 더해줘야 하는 수 0으로 초기화 
        if tmp<10:
            stack.append(tmp)
        else:
            stack.append(tmp%10) 
            add=1

elif a_length>b_length: # A와 B의 길이가 다를 때 (A가 더 클 때) 
    for i in range(b_length):
        tmp=int(A[-1-i])+int(B[-1-i])
        tmp+=add 
        add=0
        if tmp<10:
            stack.append(tmp)
        else:
            stack.append(tmp%10) 
            add=1
    # B 기준으로 돌고 나서 A는 더 돌아야 할 수들이 남아 있음 
    for j in range(a_length-b_length):
        tmp=int(A[-i-j-2])
        tmp+=add
        add=0
        if tmp<10:
            stack.append(tmp)
        else:
            stack.append(tmp%10)
            add=1

# 뒤에서부터 더해주기 
for i in range(len(stack)-1, -1, -1):
    answer+=str(stack[i])

# 마지막에서도 10 넘었을 때 
if add==1:
    answer=str(add)+answer

print(answer)
