# 힌트: 서로 다른 세 자리 수 중에 최대 수는 무엇이죠? 모든 경우를 다 해봐도 좋겠어요.
# 0은 사용하지 않는다는 걸 주의해야 해요.

n=int(input())
questions=[]
for i in range(n):
    questions.append(input().split()) # p2. 파이썬 input받은 애는 기본적으로 str 
    #questions.append(list(map(str, input().split())))

# 내가 해보려고 했던 방법: lambda 이용해서 스트라이크 많은 순서로 정렬해서
# 예를 들면 32_에서 7, 1, 5, 6.. 지워나가면서 검사.. 근데 구현 막막했음

answer=0

# str <-> int 사이에서 실수 많았음 
for number in range(987,122,-1): # MAX: 987 min: 123 
    flag=1
    if '0' in str(number): # 히든 케이스
        continue
    if str(number)[0]==str(number)[1] or str(number)[1]==str(number)[2] or str(number)[2]==str(number)[0]: # 서로 다른 숫자인지 
        continue
    for q in questions:
        strike=0
        ball=0
        for i in range(3):
            if q[0][i] in str(number):
                if str(number).index(q[0][i])==i:
                    strike+=1
                else:
                    ball+=1
                
        if strike!=int(q[1]) or ball!=int(q[2]):
            flag=0
            break
    if flag==1:
        answer+=1

print(answer)
            
            
