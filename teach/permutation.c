#include <stdio.h>

int n, a[20], used[20];

void permute(int state) {
	int i;
	if(state == n + 1) {
		for(i=1; i<=n; ++i) {
			printf("%d", a[i]);
		}
		printf("\n");
		return ;
	}
	for(i=1; i<=n; ++i) {
		if(used[i] == 1) {
			continue;
		}
		used[i] = 1;
		a[state] = i;
		permute(state + 1);
		used[i] = 0;
	}
}

int main() {
	scanf("%d", &n);
	permute(1);
	return 0;
}
