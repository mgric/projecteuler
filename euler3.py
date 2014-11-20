import math

num = 600851475143

number = math.sqrt(num)
number = int( math.floor(number))

for i in range (2, number):
	if num % i  == 0:
		num = num/i
		z=i
		i=2

print (z) 