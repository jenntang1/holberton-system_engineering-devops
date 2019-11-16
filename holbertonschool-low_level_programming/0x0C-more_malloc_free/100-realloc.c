#include "holberton.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * *_memcpy - function that copies memory area
 * @dest: letters
 * @src: letters
 * @n: integers
 * Description: Copies n bytes from memory area src to dest
 * Return: Pointer to dest
 */
char *_memcpy(char *dest, char *src, unsigned int n)
{
	/* declare iteration variable */
	unsigned int iterate;
	/* will copy up to the size of n */
	for (iterate = 0; iterate < n; iterate++)
		/* copy src to dest */
		dest[iterate] = src[iterate];
	return (dest);
}

/**
 * *_realloc - function that deallocates memory pointed to by a pointer
 * and that pointer points to new memory
 * @ptr: pointer to the memory of old_size, meaning ptr=malloc(old_size)
 * @old_size: size in bytes
 * @new_size: size in bytes
 * Description: Lookup man realloc for reference
 * Return: NULL if fail
 */
void *_realloc(void *ptr, unsigned int old_size, unsigned int new_size)
{
	/* declare variable pointer to return */
	void *newptr;
	/* call is equivalent to malloc(new_size) for values of old_size & new_size */
	if (ptr == NULL)
	{
		newptr = malloc(new_size);
		free(ptr);
		return (newptr);
	}
	/* call is equivalent to free(ptr) and return NULL */
	if (new_size == 0 && ptr != NULL)
	{
		free(ptr);
		return (NULL);
	}
	/* "added" memory shouldn't be initialized */
	if (new_size > old_size)
	{
		newptr = malloc(new_size);
		return (newptr);
	}
	/* if realloc fails the original block is untouched */
	if (new_size == old_size)
		return (ptr);
	/* allocate memory for new_size */
	newptr = malloc(new_size);
	if (newptr == NULL)
		return (NULL);
	_memcpy(newptr, ptr, old_size);
	free(ptr);
	return (newptr);
}
