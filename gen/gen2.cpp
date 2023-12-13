#include <bits/stdc++.h>
#include "testlib.h"

using namespace std;

int main(int argc, char* argv[]) {
	registerGen(argc, argv, 1);

	int N = atoi(argv[1]);
	int MIN_RANGE = atoi(argv[2]);
	int MAX_RANGE = atoi(argv[3]);

	cout << N << "\n";
	for(int i=1; i<N; ++i) {
		int state = rnd.next(0, 2);
		int l = rnd.next(MIN_RANGE, MAX_RANGE);
		int r = rnd.next(l, MAX_RANGE);
		cout << "1 " << l << " " << r << "\n";
	}
	cout << "2\n";
	return 0;
}
