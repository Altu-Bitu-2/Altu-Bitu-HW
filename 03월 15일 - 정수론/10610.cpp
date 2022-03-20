#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
	string n;
	cin >> n;
	vector<int> s;
	long long temp=0;
	
	for (int i=0; i<n.size(); i++){
	    s.push_back(n[i]-'0');
	    temp+=n[i]-'0';
	}
	
	sort(s.begin(), s.end(), greater<int>());
	
	// 30의 배수가 되는 조건 -> 각 자리 합 3의 배수 && 일의 자리 수 0
	if (temp%3!=0 || s[s.size()-1]!=0){
	    cout << -1;
	}
	
	else{
	    for (int i=0; i<s.size(); i++){
	        cout << s[i];
	    }
	    
	}
}