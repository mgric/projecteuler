import math

num  = 999999999
test = [11,12,13,14,15,16,17,18,19,20]

for i in range (2520,num,2520):
	
	if all(i % n == 0 for n in test):
		z=i
		break


print(z)
		