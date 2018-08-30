#find the posstion of prime number
i = 1
q = 0
posstion = input("enter number")
while True:
	i +=1
	s = 0
	for j in xrange(2,i):
		if i % j ==0:
			s +=1
	if s == 0:
		q +=1
		if q==posstion:
			print "Exact posstion of prime number",i
			break