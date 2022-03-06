#include <iostream>

using namespace std;

int main(void){
	ios::sync_with_stdio(false);
	cin.tie(0);

	int h, m, s; // 시, 분, 초
	cin >> h >> m >> s;
	int now = h*3600+m*60+s; // 현재 시간 초 단위로 

	int n; // 쿼리의 갯수
	cin >> n;

	int t, c; // 쿼리의 T, 몇 초 돌릴 것인지 
	for (int i=0; i<n; i++){
		cin >> t;
		if (t==1){
			cin >> c;
			now = (now+c)%86400;
			h = now/3600;
			m = (now%3600)/60;
			s = (now%3600)%60;
		}
		else if (t==2){
			cin >> c;
			now = (now-c)%86400;
			if (now<0){
				now += 86400;
			}
			h = now/3600;
			m = (now%3600)/60;
			s = (now%3600)%60;
		}
		else{ // t==3
			cout << h << " " << m << " " << s << "\n";
		}
	}
}