# Sum square of difference
s = 0
q = 0
for j in range(1,101):
	q = q+j
p = q**2
print p
for i in range(1,101):
	a = i**2
	s = s + a
print s	
p = p -s
print p