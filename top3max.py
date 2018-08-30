q = input("enter number of values") # take input from user, how many value he want to check  
r = [] # this empty list stored the value
for j in range(0,q): 
	s = input("enter number")
	r.append(s) 
print r
var = 0 # we define one variable to stored max value
for i in r: #variable i is consist of list of 'r''s value 
	if i > var: # conditio check the greatest value from a list
		var = i 
		var1 = 0
		for i in r: # another loop is check for second largest value in a list  
			if i > var1 and i !=var: # this conditon is drop the first max value and check second largest value in a list
				var1 = i
				var2 = 0
				for i in r: # thos loop is check third largest value in a list  
					if i > var2 and i !=var and i != var1: #this conditon is drop the first and second max value and check third largest value in a list
						var2 = i
print var , var1 , var2 # finally print top 3 largest value from a list storing in three variable