# find the sum of the even-valued numbers
x = input("enter number")
y = 0
z = 1
sum = 0
a = 0
for i in range(0,x):
		y = y + z
		z = y - z
		sum = y + z;
		print sum
		if sum % 2 == 0:
			a = a + sum
print a	," Sum of even numbers"