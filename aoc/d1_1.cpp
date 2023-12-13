#include <bits/stdc++.h>

using namespace std;

int main() {
	string s;
	int sum = 0;
	while(cin >> s) {
		int t = 0;
		for(int i=0; i<(int) s.size(); ++i) {
			if(isdigit(s[i])) {
				t += (s[i] - '0');
				break;
			}
		}
		t *= 10;
		for(int i=(int) s.size() - 1; i>=0; --i) {
			if(isdigit(s[i])) {
				t += (s[i] - '0');
				break;
			}
		}
		sum += t;
	}
	cout << sum << "\n";
	return 0;
}
