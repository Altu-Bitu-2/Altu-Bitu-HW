#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int string_to_int(string a){
	int sum=0;
	for (int i=0; i<a.size(); i++){
		if ((a[i])-'0'>=0 && (a[i]-'0')<=9){
			sum+=(a[i]-'0');
		}
	}
	return sum;
}

bool cmp(string a, string b){
	// 1. 길이가 다르면 짧은 것 먼저
	if (a.size()!=b.size()){
		return a.size()<b.size();
	}

	// 2. 길이가 같으면 작은 합 먼저
	int sum_a=0;
	int sum_b=0;

	sum_a=string_to_int(a);
	sum_b=string_to_int(b);
	
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
