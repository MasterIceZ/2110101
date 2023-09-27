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

	int q, found = 0;
	scanf("%d", &q);
	for(i=0; i<n; ++i) {
		for(j=0; j<n; ++j) {
			if(a[i][j] == q) {
				printf("[%d %d] ", i, j);
				found = 1;
			}
		}
	}
	if(found == 0) {
		printf("Not found");
	}

	printf("\n");
	return 0;
}
