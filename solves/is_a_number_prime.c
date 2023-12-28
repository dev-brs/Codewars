//https://www.codewars.com/kata/5262119038c0985a5b00029f

#include <stdbool.h>
#include <math.h>

bool is_prime(int num)
{
  if (num <= 1)
    return false;
  if (num == 2)
    return true;
  for(int i = 2; i < (sqrt(num)+1);i++)
  {
    if (num % i == 0)
      return false;
  }
  return true;
}