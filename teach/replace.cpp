#include <stdio.h>

int main() {
	int n, m;
	scanf("%d %d", &n, &m);
	
	int i, j, a[n][m];
	for(i=0; i<n; ++i) {
		for(j=0; j<m; ++j) {
			scanf("%d", &a[i][j]);
		}
	}

	int q, want;
	scanf("%d", &q);
	for(j=0; j<m; ++j) {
		scanf("%d", &want);
		a[q][j] = want;
	}

	for(i=0; i<n; ++i) {
		for(j=0; j<m; ++j) {
			printf("%d ", a[i][j]);
		}
		printf("\n");
	}
	return 0;
}
