import sys
import heapq as hq
input = sys.stdin.readline

"""
[Yonsei TOTO]
 수강 인원이 미달일 때 필요한 마일리지는 0이 아니라 1
 1. 각 과목을 듣기 위해 필요한 최소 마일리지를 계산 (정렬)
 2. 가장 마일리지가 적게 드는 과목부터 수강 신청 (우선순위 큐 or 정렬)
"""

def maxClass(m, min_heap):
    count = 0 # 과목 개수 저장할 변수 
    # 더이상 들을 과목이 없거나, 마일리지가 모자르면 반복문 탈출
    while min_heap and min_heap[0] <= m:
        m -= hq.heappop(min_heap) # 가지고 있는 총 마일리지에서 최소 마일리지 삭제 
        count += 1 # 과목 개수 1 더해줌

    return count # 과목 개수 return 


# 입력
n, m = map(int, input().split()) # n: 과목 개수, m: 가지고 있는 마일리지 
min_heap = []   # 필요한 최소 마일리지 저장할 최소 힙

for _ in range(n):
    # 입력
    p, l = map(int, input().split()) # p: 신청자 수, l: 수강 정원 수 
    mileage = list(map(int, input().split())) # 현재 마일리지 

    # 수강인원보다 적게 수강신청한 경우 
    if p < l:
        hq.heappush(min_heap, 1) # 1 필요 
        continue # 다음 반복으로 

    mileage.sort(reverse=True) # 내림차순 정렬 
    # l번째로 마일리지를 많이 넣은 사람과 같은 양의 마일리지를 넣어야 수강 가능
    hq.heappush(min_heap, mileage[l-1])

# 연산 + 출력
print(maxClass(m, min_heap))
