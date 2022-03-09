#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(string a, string b){
	// 1. 길이가 다르면 짧은 것 먼저
	if (a.size()!=b.size()){
		return a.size()<b.size();
	}

	// 2. 길이가 같으면 작은 합 먼저
	int sum_a=0;
	int sum_b=0;
	for (int i=0; i<a.size(); i++){
		if ((a[i]-'0')>=0 && (a[i]-'0')<=9){
		    sum_a+=(a[i]-'0');
		}
	}
	for (int i=0; i<b.size(); i++){
		if ((b[i]-'0')>=0 && (b[i]-'0')<=9){
		    sum_b+=(b[i]-'0');
		}
	}
	if (sum_a!=sum_b){
	    return sum_a<sum_b;
	}

	// 3. 사전순 
	return a<b;

}

int main(void){
	int n;
	cin >> n;
	vector<string> guitars(n);
	for (int i=0; i<n; i++){
		cin >> guitars[i];
	}
	
	sort(guitars.begin(), guitars.end(), cmp);

	for (int i=0; i<n; i++){
		cout << guitars[i] << "\n";
	}

}
