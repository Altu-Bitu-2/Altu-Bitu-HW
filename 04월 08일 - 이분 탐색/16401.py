import sys
input = sys.stdin.readline

"""
 [과자 나눠주기]
 n개의 과자가 있을 때 m명의 조카에게 각각 같은 길이로 줄 수 있는 과자의 최대 길이를 구하는 문제
 -> 특정 과자 길이에 대하여 m명의 조카에게 나누어 줄 수 있는가?
 left: 과자 길이의 최솟값 -> 1
 right: 과자 길이의 최댓값
"""

# 내림차순 정렬된 snacks 리스트에서 length 길이의 과자를 몇개 만들 수 있는지 개수를 세어 리턴하는 함수
def split_snack(length, snacks):
    count = 0 # 0으로 초기화 
    for l in snacks: # snacks 순회하면서 
        if l < length: # length가 더 길면 더 이상 만들 수 없으므로
            return count # 지금까지 더해진 count return 
        count += l // length # length보다 작으면 만들 수 있는 갯수만큼 더해주기 

    return count # 만들 수 있는 갯수 return 

# 이분 탐색 
def binary_search(m, snacks):
    left = 1 # 과자 길이의 최솟값 
    right = snacks[0] # snacks의 가장 큰 값 
    while left <= right: # left<=right인 동안
        mid = (left + right) // 2 # 이분 탐색 위해 left와 right의 중간 값 설정 
        if split_snack(mid, snacks) >= m: # 만들 수 있는 갯수가 m보다 크다면 
            left = mid + 1 # 더 커져야 하므로 최솟값 키워주기
        else: # 만들 수 있는 갯수가 m보다 작으면 
            right = mid - 1 # 더 작아져야 하므로 최댓값 줄여주기 
    return left - 1 # left-1 return 

m, n = map(int, input().split()) # m: 조카의 수, n: 과자의 수
snacks = list(map(int, input().split())) # 과자의 길이 
snacks.sort(reverse=True)   # 내림차순 정렬

print(binary_search(m, snacks)) # 막대 과자의 최대 길이 출력 
