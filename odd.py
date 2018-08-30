# this program print the how many even or odd number are there  in a list
r = [1,2,3,4,5,6,7,8,9]
odd = 0
even = 0
for i in range(0,len(r)):
	if r[i] % 2 == 0:
		even +=1
	else:
		odd +=1
print "even number" , even
print "odd number" , odd