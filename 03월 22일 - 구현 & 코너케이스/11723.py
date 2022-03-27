# 1. s를 리스트로 구현 -> 메모리 초과
# 2. 힌트 참고 -> 모르겠음.. 
# 3. 구글링 -> s를 set으로 구현하고 add와 discard 사용하여 if문 줄임 -> 메모리 초과

n=int(input())
operations=[]
for i in range(n):
    operations.append(input())

s=set([])

for operation in operations: 
    a=(operation.split())[0] # 수행해야 할 연산의 종류
    
    if a=="all":
        s=set(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
        continue
    
    elif a=="empty":
        s=set([])
        continue
        
    elif a=="add" or a=="remove" or a=="check" or a=="toggle":
        b=(operation.split())[1] # x -> str로 받아진 것 주의! 

    if a=="add":
        #if b not in s:
        s.add(b)

    elif a=="remove":
        #if b in s:
        s.discard(b) # discard 쓰는 이유: remove와 달리 discard는 없어도 정상 종료

    elif a=="check":
        if b in s:
            print(1)
        else:
            print(0)

    elif a=="toggle":
        if b in s:
            s.discard(b)
        else:
            s.add(b)
