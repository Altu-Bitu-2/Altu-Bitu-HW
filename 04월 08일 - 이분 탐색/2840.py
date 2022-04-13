## 바퀴에 있는 알파벳은 중복될 수 없다 => 히든 케이스
## 첫 번째 시도: 히든 케이스 고려 못함
## 두 번째 시도: 히든 케이스 고려했으나 if flag==1 안의 else 처리 못함 

from collections import Counter

import sys
input=sys.stdin.readline

n,k=map(int, input().split())
rotations=[input().split() for _ in range(k)]

wheel=[" "]*n
wheel[0]=rotations[0][1]
now=0

flag=1

for i in range(1,k): 
    now=(now+int(rotations[i][0]))%n
    if wheel[now]!=" " and wheel[now]!=rotations[i][1]:
        flag=0
        break 
    wheel[now]=rotations[i][1]

if flag==1:
    temp=''.join(wheel)
    temp=temp.replace(" ","")
    # " " 제외 가장 많이 등장한 글자의 갯수가 2번 이상일 경우 
    if Counter(temp).most_common()[0][1]>=2: 
        print("!")
    else: 
        # 출력은 시계 반대방향으로
        answer=""
        while len(answer)<n:
            answer+=wheel[now]
            now-=1

        answer=answer.replace(" ","?")
        print(answer)
else:
    print("!")
