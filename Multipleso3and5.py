#Find the sum of all the multiples of 3 or 5 below user input numbers
x = input("enter number")
sum = 0
for i in range(1,x):
	if i % 3 == 0 or i % 5==0:
		sum = sum + i;
print sum
