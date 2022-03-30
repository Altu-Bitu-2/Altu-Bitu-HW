# 1. 문제 이해가 진짜 오래 걸렸고 정말 오래 걸려서 풀었는데 -> 시간초과
# 2. 힌트 참고 -> 가장 먼저 올라온 로봇은 항상 내리는 위치와 가깝다 -> 아랫 줄에는 갈 수 없으니 윗 줄만 검사하면 됨 

import sys
input=sys.stdin.readline

from collections import deque

n,k=map(int,input().split())
belt=list(map(int, input().split()))
queue=deque(belt)

robots=deque([False]*len(belt)) # True이면 로봇이 있음 
stage=1 # 현재 단계

while True:
    # 1. 회전할 때는 내구도 감소시킬 필요 없음 
    queue.rotate(1) # rotate(n): n이 양수면 오른쪽으로, 음수면 왼쪽으로 회전
    robots.rotate(1) # 로봇도 같이 돌아가기
    if robots[n-1]==True:
        robots[n-1]=False
    #print(queue)
    #print(robots)
    # 2.
    if sum(robots)>0:
        check=robots.count(True)
        temp=0
        # 로봇이 아랫 줄에는 갈 수가 없음 
        for i in range(n-1,-1,-1): # 가장 먼저 벨트에 올라간 로봇부터! (4번 테스트 케이스)
            if robots[i]==True:
                if robots[i+1]==False and queue[i+1]>=1:
                    if i+1==n-1:
                        robots[i+1]=False
                    else:
                        robots[i+1]=True
                    robots[i]=False
                    queue[i+1]-=1
                    temp+=1
                    if temp==check:
                        break
    #print(queue)
    #print(robots)
    # 3.
    if queue[0]!=0:
        robots[0]=True
        queue[0]-=1
    #print(queue)
    #print(robots)
    # 4.
    if queue.count(0)>=k:
        break
    stage+=1
    #print(queue)
    #print(robots)
    #print("**************")

print(stage)
