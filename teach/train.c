#include <stdio.h>
#include <stdbool.h>

int count[110];

int main() {
	int n, m, i, j, p, _, l, r, v, answer = 0;
	bool ok;
	scanf("%d %d %d", &n, &m, &p);
	for(i=1; i<=m; ++i) {
		scanf("%d %d %d %d", &_, &l, &r, &v);
		ok = true;
		for(j=l; j<r; ++j) {
			if(count[j] + v > p) {
				ok = false;
				break;
			}
		}
		if(ok == false) {
			answer += i;
			continue;
		}
		for(j=l; j<r; ++j) {
			count[j] += v;
		}
	}
	printf("%d\n", answer);
	return 0;
}
