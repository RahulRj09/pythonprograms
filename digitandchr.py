s = raw_input("enter value") # take alphanumeric string from a user  
r = 0 # we take a two variable 'r' and 'j' to count the how many numbers and alphabets are ther in a string.
j = 0
for i in s: # 'i' variable is consist the value of 's'. 
	if i.isdigit(): # condition check how many digit in a string 
		r +=1
	elif i.isalpha(): # condition check how many alphabet in a string
		j +=1
print "numbers " ,r," Strings",j