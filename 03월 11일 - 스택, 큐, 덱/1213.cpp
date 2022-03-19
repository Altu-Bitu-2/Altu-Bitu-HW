// 설명 참고: https://yabmoons.tistory.com/162

#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

int main(){
	string s;
	cin >> s;
	map<char,int> m;
	for (int i=0; i<s.size(); i++){
		m[s[i]]+=1;
	}

	int odd_n=0; // 홀수 개인 알파벳의 개수 
	for (auto a:m){
		if (a.second%2==1){
			odd_n+=1;
		}
	}

	if (odd_n>=2){
		cout << "I'm Sorry Hansoo";
	}
	else{ // 홀수가 1개 or 0개
		// 여기 알고리즘이 어려움 ★ 
		string answer="";
		string tmp="";
		for (auto a:m){
			for (int i=0; i<a.second/2; i++){
				answer+=a.first;
			}
		}
		tmp=answer;
		for (auto a:m){
			if (a.second%2==1){
				answer+=a.first;
			}
		}
		reverse(tmp.begin(), tmp.end());
		answer+=tmp;
		cout << answer;
	}
}