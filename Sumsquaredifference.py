# Sum square of difference
s = 0
q = 0
square = input("upto how much you want square and square difference")
for j in range(1,square+1):
	q = q+j
p = q**2
print p
for i in range(1,square+1):
	a = i**2
	s = s + a
print s	
p = p -s
print p