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
	/* declare variable for child process */
	pid_t child;
	/* create child process */
	child = fork();
	/* if child process is a zombie, then print error msg */
	if (child > 0)
	{
		fprintf(stderr, "Zombie process created, PID: %d\n", child);
		exit(1);
	}
	/* if child process is zero, then exit normally */
	if (child == 0)
	{
		exit(0);
	}
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
