#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	vector<int> card={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20};
	int start, end;

	for (int i=0; i<10; i++){
		cin >> start >> end;
		reverse(card.begin()+start-1, card.begin()+end);
	}
	
	// 출력 
	for (int i=0; i<20; i++){
	    cout << card[i] << " ";
	}
}