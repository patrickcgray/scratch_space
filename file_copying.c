#include <stdio.h>

#define IN 	1
#define OUT	0

main() {
	int c, state;

	state = OUT;
	while ((c = getchar()) != EOF) {
		if (c == ' ' || c == '\n' || c == '\t') {
			state = OUT;
		}
		else if (state == OUT) {
			printf("\n");
			putchar(c);
			state = IN;
		}
		else
			putchar(c);
		
		if (c == '\n')
			printf("\n");
	}
}