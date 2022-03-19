#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <map>

using namespace std;

// 산술평균
int arithmeticMean(vector<int> v){
	int s=0;
	for (int i=0; i<v.size(); i++){
		s+=v[i];
	}
	return round((double)s/double(v.size()));
}

// 중앙값
int median(vector<int> v){
	return v[v.size()/2];
}

// 최빈값 ★ 
int mode(vector<int> v){
	map<int,int> m;
	for (auto a:v){
		m[a]+=1;
	}
	int max=0;
	vector<int> maxVal;
	for (auto a:m){
		if (a.second>=max){
			// 34~38 여기 처리를 생각 못함 
			if (a.second!=max){
				max=a.second;
				maxVal.clear();
			}
			maxVal.push_back(a.first); // 
		}
	}
	if (maxVal.size()>=2){
		return maxVal[1];
	}
	return maxVal[0];
}

// 범위
int range(vector<int> v){
	return v[v.size()-1]-v[0];
}

int main(){
	int n;
	cin >> n;
	vector<int> v(n);
	for (int i=0; i<n; i++){
		cin >> v[i];
	}

	sort(v.begin(), v.end());

	cout << arithmeticMean(v) << "\n";
	cout << median(v) << "\n";
	cout << mode(v) << "\n";
	cout << range(v) << "\n";

}