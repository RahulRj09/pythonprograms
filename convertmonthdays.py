# this program check which month is how many days are contain
# i take a 2 list it contain number of months
listof31daymonths = ["January","March","May","July","August","October","December"]
listof30daymonths = ["April","June","September","November"]
user = input("Enter a months: January, February, March, April, May, June, July, August, September, October, November, December"  )
for i in listof31daymonths: # this loop check only 31 days month
	if user in listof31daymonths: # if user input is in a list of 31 days month then it will print 31 days
		print ("31 day")
		break
for j in listof30daymonths:# his loop check only 30 days month
	if user in listof30daymonths: # if user input is in a list of 30 days month then it will print 30 days
		print ("30 day")
		break
	else: # if user put the feburary month it will we goes on else condition print 28 and 29 days
		print ("28/29 day")
		break