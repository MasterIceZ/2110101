#include <stdio.h>

int main() {
	int n, m, i, j;
	scanf("%d %d", &n, &m);
	
	int a[n][m];
	for(i=0; i<n; ++i) {
		for(j=0; j<m; ++j) {
			scanf("%d", &a[i][j]);
		}
	}

	// 1 2 3
	// 4 5 6
	// 7 8 9
	//
	// 1 4 7
	// 2 5 8
	// 3 6 9
	
	for(j=0; j<m; ++j) {
		for(i=0; i<n; ++i) {
			printf("%d ", a[i][j]);
		}
		printf("\n");
	}

	printf("\n");
	return 0;
}
