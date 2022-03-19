// 힌트 참고함 

#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;

int main(void){
	int n;
	cin >> n;

	vector<int> v(n); // 최종 카드 상태  
	for (int i=0; i<n; i++){
		cin >> v[i];
	}

	reverse(v.begin(), v.end());
	deque<int> d; // 정답을 담을 deque

	for (int i=0; i<n; i++){
		// 1. 제일 위의 카드 1장 내려놓기 -> 맨 뒤에 넣기
		if (v[i]==1){
			d.push_back(i+1);
		}

		// 2: 위에서 두 번째 내려놓기 (2장 이상일 때) 
		// -> 맨 뒤 잠시 뺐다가 그 다음 뒤 맨 뒤에 넣고 다시 뺀 애 맨 뒤에
		else if (v[i]==2){
			int tmp=d.back();
			d.pop_back();
			d.push_back(i+1);
			d.push_back(tmp);
		}

		// 3. 제일 밑 내려놓기 (2장 이상일 때) -> 맨 앞에 넣기
		else if (v[i]==3){
			d.push_front(i+1);
		}

	}
 
	while (!d.empty()){
		int tmp=d.back();
		cout << tmp << " ";
		d.pop_back();
	}
}