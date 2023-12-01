#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>


int parse_line(char *line, ssize_t read) { 
  int first_digit = 0;
  int last_digit = 0;

  for (ssize_t i = 0; i < read; i++) {
    if (isdigit(line[i])) {
      first_digit = line[i] - '0';
      break;
    }
  }

  for (ssize_t i = read - 1; i >= 0; i--) { 
    if (isdigit(line[i])) {
      last_digit = line[i] - '0';
      break;
    }
  }

  return first_digit * 10 + last_digit;
}

int main(void) {
  FILE *fp;
  char *line = NULL;
  size_t len = 0;
  ssize_t read;

  fp = fopen(
      "/Users/andrewstelmach/Desktop/advent-of-code-2023/day01/input.txt", "r");
  if (fp == NULL) {
    printf("Could not open file\n");
    exit(EXIT_FAILURE);
  }

  int sum = 0;
  while ((read = getline(&line, &len, fp)) != -1) {
    int result = parse_line(line, read); 
    printf("%d\n", result);
    sum += result;
  }

  fclose(fp);

  if (line)
    free(line);

  printf("%d\n", sum);

  return 0;
}
