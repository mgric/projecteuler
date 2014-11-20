import math

num = [1,1]
z=0
for i in range (2,10000000):
	 
	num.append(num[i-1]+ num[i-2] ) 

	if num [i] > 4000000:
		break

for i in range( len(num)):
	if num[i] % 2 == 0:
		z=z +num[i]


print (z)	
print (num)