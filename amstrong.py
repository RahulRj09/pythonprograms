#how to find out amstrong number 
for i in range(2000):
	amstrong=list(str(i)) #we convert input in string then it will put in a list
	sum1=0
	for j in range(len(amstrong)):# this loop convert string value into intger from a list because we wont add number separetly
		s=int(amstrong[j])
		d=s**len(amstrong)
		sum1=sum1+d
	if i==sum1: #finaly if sum is equal to our orignal number / user input then it is amstrong number
		print sum1,"Is amstrong Number"