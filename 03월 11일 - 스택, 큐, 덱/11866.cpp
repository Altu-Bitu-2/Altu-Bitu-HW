// 샘플 코드 보고 추가 제출 

#include <iostream>
#include <queue>
#include <vector>

using namespace std;

vector<int> simulation(int k, queue<int> &q) {
    vector<int> result; //요세푸스 순열
    int cnt = 0; //카운트 변수

    while (!q.empty()) { // 큐는 auto로 순회할 수 없어서 empty할 때까지 뽑아야 함 
        int x = q.front(); // 맨 앞 원소 가리키고
        q.pop(); // 뽑기 
        cnt++; // 몇 번째인지 
        if (cnt == k) { //k번째 pop하는 원소라면
            result.push_back(x); // result에 넣기 
            cnt = 0; // 넣었으니 몇 번째인지 초기화 
            continue;
        }
        q.push(x); // pop한 원소 다시 큐 뒤로 push
    }
    return result;
}

/**
 * 1. 큐에 1 ~ N까지 값 초기화
 * 2. 이후 k 번째 사람 찾기 위해 pop, push 반복
 * 3. k번째 pop 일 경우 요세푸스 순열에 저장, 이후 원소 제거 (다시 push 하지 않음!)
 */

int main() {
    int n, k; // n: 사람 수, k: 제거할 사람이 몇 번째인지
    queue<int> q; // ★원 -> 원형 큐 아이디어

    //입력
    cin >> n >> k;
    for (int i = 1; i <= n; i++) { //큐 초기화
        q.push(i);
    }
    //연산
    vector<int> result = simulation(k, q); // 요세푸스 순열
    //출력
    cout << '<';
    for (int i = 0; i < result.size() - 1; i++) {
        cout << result[i] << ", ";
    }
    cout << result[result.size() - 1] << '>';
    return 0;
}