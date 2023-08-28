#include <stdio.h>

int main() {
	char s;
	scanf("%c", &s);
	switch(s) {
		case 'M':
			printf("Mastery\n");
			break;
		case 'm':
			printf("Mastery\n");
			break;
		case 'H':
			printf("Harmony\n");
			break;
		case 'h':
			printf("Harmony\n");
			break;
		default:
			printf("Invalid charactor");
	}
	return 0;
}
