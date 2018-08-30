# this program print the how many even or odd number are there  in a list
x=[10,54,86,41,1,23,45]
a=[]
b=[]
i=0
while i<len(x):
	if x[i]%2==0:
		a.append(x[i])
	else:
		b.append(x[i])
	i+=1
print "total even number is",len(a)
print "total odd number is",len(b)		