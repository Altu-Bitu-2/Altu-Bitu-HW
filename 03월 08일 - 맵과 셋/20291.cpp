#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main(void){
	map<string,int> file;

	int n;
	cin >> n; // 파일의 개수

	vector<string> notebook_files(n);
	for (int i=0; i<n; i++){
		cin >> notebook_files[i];
	}

	// Python처럼 . 기준으로 string 나눠서 뒷부분만 가리키고 싶었지만
	// C++에서는 이럴 경우 find랑 substr을 같이 사용해서 분리함 
	for (int i=0; i<n; i++){
		int idx=notebook_files[i].find(".");
		string key=notebook_files[i].substr(idx+1);
		file[key]+=1; // map 밸류 이미 0으로 초기화되어 있음 
	}

	// 맵 순회하는 법: auto, first, second 활용 
	for (auto f:file){
	    cout << f.first << " " << f.second << "\n";
	}
}