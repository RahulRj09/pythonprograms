#find the Summation of prime numbers
q = 0
prime = input("enter number user want Summation of prime number")
for i in range(2,prime):
	s = 0
	for j in range(2,i):
		if i % j == 0:
			s +=1
	if s ==0:
		print "prime",i
		q = q + i
print q
