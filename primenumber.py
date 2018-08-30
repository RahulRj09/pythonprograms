# this program check number is prime or not
prime = input("enter number is prime or not")
s = 0
for i in range(2,prime):
	if prime % i == 0:
		s +=1
if s == 0:
	print "number is prime"
else:
	print "nmuber not prime"