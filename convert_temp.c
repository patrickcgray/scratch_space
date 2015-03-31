#include <stdio.h>

main()
{
	float fahr, celsius;
	float lower, upper, step;

	lower = 0;
	upper = 300;
	step = 20;

	fahr = upper;			
	printf("%4s\t%7s\n", "Fahr", "Cel ");
	while (fahr >= lower) {
		celsius = 5.0 * (fahr-32.0) / 9.0;
		printf("%4.0f\t%6.1f\n", fahr, celsius);
		fahr = fahr - step;
	}
}