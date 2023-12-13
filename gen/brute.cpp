#include <bits/stdc++.h>

using namespace std;

const int MxN = 1e9 + 10;
bitset<MxN> b;

int main() {
	cin.tie(nullptr)->ios::sync_with_stdio(false);
	int n, opr, l, r, cnt = 0;
	cin >> n;
	for(int i=1; i<=n; ++i) {
		cin >> opr;
		if(opr == 1) {
			cin >> l >> r;
			int c = 0, last = 0;
			c += (b[l] == false && b[l - 1] == true);
			c += (b[r] == false && b[r + 1] == true);
			for(int x=l; x<=r; ++x) {
				if(b[x] == true && last == 0) {
					c += 1;
					last = 1;
				}
				else if(b[x] == false) {
					b[x] = true;
					last = 0;
				}
			}
			cnt += 1 - c;
		}
		else {
			cout << cnt << "\n";
		}
	}
	return 0;
}
