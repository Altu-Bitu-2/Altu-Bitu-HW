#include <iostream>
#include <map>

using namespace std;

int main(void){
	// Q. IDE를 돌릴 때 인풋과 아웃풋이 섞여 나올 때 해결 방법
	// 3월 4일 정렬 12840번은 ios::sync_with_stdio(false); cin.tie(0);
	// 차이점이 뭔가요? 
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

	int n;
	cin >> n;

	for (int i=0; i<n; i++){
		int n_cloth; // 해빈이가 가진 의상의 수
		cin >> n_cloth;

		map<string,int> coordinate;
		for (int j=0; j<n_cloth; j++){
			string tmp_a, tmp_b;
			cin >> tmp_a >> tmp_b; // cin은 공백 기준임 
			coordinate[tmp_b]+=1;
		}

		int answer=1;
		for (auto c:coordinate){
			answer*=(c.second+1);
		}
		answer-=1;
		cout << answer << "\n";
	}
}