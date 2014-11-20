import math
z=0
m=0
for i in range (0,101,1):
	z+=i
	m=m+i**2

ans = m-z**2

print(ans)