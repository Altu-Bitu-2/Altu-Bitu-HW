# 1. 직접 거듭제곱해서 나머지에 따라 출력 -> 시간초과

# 2. 일의 자리 수 규칙
# 1 -> 항상 1
# 2 -> 4 -> 8 -> 6 -> ..
# 3 -> 9 -> 7 -> 1 -> ..
# 4 -> 6 -> ..
# 5 -> 항상 5
# 6 -> 항상 6
# 7 -> 9 -> 3 -> 1 -> ..
# 8 -> 4 -> 2 -> 6 -> ..
# 9 -> 1 -> ..
# 0 -> 항상 0 (0이 아니라 10 출력해야 함!★ 오히려 시간초과 떴던 처음에는 고려했는데 규칙 복잡해지면서 빼먹음 ㅠㅠ)

n=int(input())

data=[]
for i in range(n):
    data.append(list(input().split()))

for i in range(len(data)):
    data[i][0]=data[i][0][-1] # 일의 자리 수만 추출 
    k=data[i][0]
    if k=="1" or k=="5" or k=="6":
        print(k)
    elif k=="2":
        temp=["2","4","8","6"]
        print(temp[int(data[i][1])%4-1])
    elif k=="3":
        temp=["3","9","7","1"]
        print(temp[int(data[i][1])%4-1])
    elif k=="7":
        temp=["7","9","3","1"]
        print(temp[int(data[i][1])%4-1])
    elif k=="8":
        temp=["8","4","2","6"]
        print(temp[int(data[i][1])%4-1])
    elif k=="4":
        temp=["4","6"]
        print(temp[int(data[i][1])%2-1])
    elif k=="9":
        temp=["9","1"]
        print(temp[int(data[i][1])%2-1])
    elif k=="0":
        print("10")
