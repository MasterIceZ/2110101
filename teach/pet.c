#include <stdio.h>

int main() {
	int i, j, x, sum, max = 0, idx = 0;
	for(i=0; i<5; ++i) {
		for(j=0; j<4; ++j) {
			scanf("%d", &a[i][j]);
		}
	}
	for(i=0; i<5; ++i) {
		sum = 0;
		for(j=0; j<4; ++j) {
//			scanf("%d", &x);
//			sum += x;
			sum += a[i][j];
		}
		if(sum > max) {
			max = sum;
			idx = i + 1;
		}
	}
	printf("%d %d\n", idx, max);
	return 0;
}
