#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
	int answer=0;

	int n;
	cin >> n; 

	vector<int> a(n);
	for (int i=0; i<n; i++){
		cin >> a[i];
	}

	vector<int> b(n);
	for (int i=0; i<n; i++){
		cin >> b[i];
	}

	sort(a.begin(), a.end());
	sort(b.begin(), b.end(), greater<int>());

	for (int i=0; i<n; i++){
		answer+=a[i]*b[i];
	}

	cout << answer;
}