#include <stdio.h>
#include <string.h>

char s[220], t[220], cipher[10][220];

int main() {
	int n, m, i, j, cnt;
	scanf("%d %d %[^\n]", &n, &m, s);
	int pt = 0, len = strlen(s);
	for(i=0; i<len; ++i) {
		if(s[i] == ' ') {
			continue;
		}	
		t[pt++] = s[i];
	}	
	len = strlen(t);
	int nn = len / n;
	if(m == 1) {
		for(i=0; i<len; ++i) {
			cipher[i / nn][i % nn] = t[i];
		}
		for(i=0, j=0, cnt=0; cnt<len; ++cnt) {
			printf("%c", cipher[i][j]);
			i++;
			if(i == n) {
				j++;
				i=0;
			}
		}
	}	
	else {
		for(i=0, j=0, cnt=0; cnt<len; ++cnt) {
			cipher[i][j] = t[cnt];
			i++;
			if(i == n) {
				j++;
				i=0;
			}
		}
		for(i=0; i<len; ++i) {
			printf("%c", cipher[i / nn][i % nn]);
		}
	}
	printf("\n");
	return 0;
}
