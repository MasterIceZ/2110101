#include <stdio.h>

int n;
char a[20];

void rec(int state) {
	int i;
	for(i=1; i<state; ++i) {
		printf("%c", a[i]);
	}
	printf("\n");
	if(state == n + 1) {
		return ;
	}
	char nxt;
	for(nxt=a[state - 1]+1; nxt<='a'+n-1; ++nxt) {
		a[state] = nxt;
		rec(state + 1);
	}
}

int main() {
	scanf("%d", &n);
	char i;
	for(i='a'; i<='a'+n-1; ++i) {
		a[1] = i;
		rec(2);
	}
	return 0;
}
