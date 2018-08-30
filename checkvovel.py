#this program is check in a string  wether vovels or consonant
vovellist = ['a','i','o','e','u','A','I','O','E','U'] #this list shows all vovels
userword = raw_input("enter String") # we take input from user
for i in range(0,len(userword)): # loop use for sperate string in one chr according there index  
	if userword[i] in vovellist: # if chr is present in vovellist then it will gives the output as a vovel else chr is consonant 
		print  userword[i],"is vovel"
	else:
		print  userword[i],"is consonant"