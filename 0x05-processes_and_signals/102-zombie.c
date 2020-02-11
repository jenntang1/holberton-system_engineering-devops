#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int infinite_while(void);

/**
 * main - function that creates zombie processes
 * Return: 0
 */
int main(void)
{
	/* declare iteration variable */
	int create = 0;
	/* declare variable for child process */
	pid_t child;

	while (create < 5)
	{
		create++;
		/* create child process */
		child = fork();
		/* if child process is a zombie, then print error msg */
		if (child > 0)
		{
			fprintf(stdout, "Zombie process created, PID: %d\n", child);
		}
		/* if child process is zero, then exit normally */
		if (child == 0)
		{
			exit(0);
		}
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - function that creates an infinite loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
