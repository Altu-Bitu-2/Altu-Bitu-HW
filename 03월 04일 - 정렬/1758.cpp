#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
	int n; // 사람 수
	cin >> n;
	vector<int> tip(n);
	long long answer=0; // 알고리즘 문제 풀 때 언제 int(X) long long(O)인지 궁금해요★

	for (int i=0; i<n; i++){
		cin >> tip[i];
	}

	sort(tip.begin(), tip.end(), greater<int>()); // 팁 내림차순 정렬 

	for (int i=0; i<n; i++){
		if (tip[i]-i>0){
			answer+=tip[i]-i;
		}
	}

	cout << answer;

}