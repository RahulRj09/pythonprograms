# this program print fibonacci series
a = 0
b = 1
c = 0
for i in range(1,51):
	c = a + b
	print c
	a = a + b
	b = a - b