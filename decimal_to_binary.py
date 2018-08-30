#   Decimal to Binary conversion
n=input('please enter the no. in decimal format: ')
x=n
list1=[] #empty list store the reminder of input
while (n>0): # loop is going on upto n=1 and n=0 it will be stop 
    a=(n%2) 
    list1.append(a) # reminder of a is stored on list1  
    n=(n-a)/2
k.append(0)
string=""
for j in range(len(k)-1,-1,-1): # we start the loop revers because binary number is print on revers order
    string=string+str(k[j]) 
print 'The binary no. for',x, 'is',string

#     Binary to Decimal conversion

n=raw_input("enter number Binary") #we take string value because of calculating the sum of all binary numbers. 
Z=[] # we take a empty list because of storing the value  
for i in range(len(n)-1,-1,-1): #we start the loop in revers order because of last index is consit of 2 power is 0,1,2,and so on 
	Z.append(n[i])
dec=0
for j in range(len(Z)):
	if int(Z[j])==1: # if z[i] is contain 1 then it's perform 2's power of index of list 'z'
		s=2**j
		dec=dec+s # according to conversion of BtoD we add the all possible numbers they consist of 1.
print "Decimal number is",dec
		