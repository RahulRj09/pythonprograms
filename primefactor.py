#find prime factor
primefactor = input("enter a number")
for j in xrange(2,primefactor):
	s = 0
	for i in xrange(2,j):
		if j % i ==0:
			s +=1
	if s == 0:
		if  primefactor % j == 0:
			print j
			print "prime factor" 