#include <stdio.h>

main() {
	int found_it;
	int seven = 7;
	int j = 0;
	int i;

	for (i = 0; i< 20; i++) {

		j = j + 1;	
		j = j % 7;
		printf("%d", j);
	}


	printf("done");
}

