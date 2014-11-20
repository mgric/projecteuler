import math

ans=0

for a in range (0, 1000):
	for b in range (a+1,1000):

		if a + b + math.sqrt(a**2+b**2) == 1000:
			ans = a*b*math.sqrt(a**2+b**2)
			c=a
			d=b
			break


print c 
print d
print math.sqrt(c**2+d**2)
print ans