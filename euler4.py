import math

max = 999
min = 100

maxk = 0

for i in range (999,min,-1):
	for j in range (999,i-1,-1):
		k = i*j
		
		if str(k) == str (k) [::-1] and k>maxk:
			maxk=k
			


print (maxk)
