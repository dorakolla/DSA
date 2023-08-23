
#Factor Pairs: To determine if a number n is prime, you need to check if it's divisible by any number between 2 and n-1. 
#However, if there are two factors a and b of n such that a * b = n,
# at least one of those factors must be less than or equal to the square root of n.
#This is because if both were greater than the square root, their product would be greater than n.
import math
def primeNumber(n):
	if n<=1:
		return False
	for i in range(2,int(math.sqrt(n)+1)):
		if n%i==0:
			return False
	return True

print(primeNumber(10))
