#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	vector<int> card(20);
	for (int i=0; i<20; i++){
		card[i]=i+1;
	}
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