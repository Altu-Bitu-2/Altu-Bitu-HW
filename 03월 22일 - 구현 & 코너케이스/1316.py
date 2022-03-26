n=int(input())
words=[]
for i in range(n):
    words.append(input()) 

# pp 이런 거 p로 합치고 
# 한 글자씩 비교해보면서 다시 나오면 안 됨 

answer=0

for i in range(len(words)): 
    for j in range(len(words[i])-1):
        if words[i][j]==words[i][j+1]:
            # 연속으로 나오면 공백으로 바꿔줌 
            words[i]=words[i].replace(words[i][j]," ",1) 

for i in range(len(words)):
    words[i]=words[i].replace(" ","") # 공백 제거 
    
for word in words:
    flag=1
    temp=[]
    for i in range(len(word)):
        if word[i] in temp: # 떨어져서 나타났음 -> 그룹 단어 아님 
            flag=0
            break
        else:
            temp.append(word[i])
    if flag==1:
        answer+=1

print(answer)
