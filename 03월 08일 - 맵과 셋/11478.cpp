#include <iostream>
#include <set>

using namespace std;

int main(void){
	string s;
	cin >> s;

	set<string> answer;

	for (int i=0; i<s.size(); i++){
		string str="";
		for (int j=i; j<s.size(); j++){
			str+=s[j];
			answer.insert(str);
		}
	}

	cout << answer.size();	
}