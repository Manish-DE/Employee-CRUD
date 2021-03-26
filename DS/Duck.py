# Python program to check whether a number is Duck Number or not. 

# Function to check whether 
# the given number is duck number or not. 
def check_duck(num) : 

	# Length of the number(number of digits) 
	n = len(num) 
	
	# Ignore leading 0s 
	i = 0
	while (i < n and num[i] == '0') : 
		i = i + 1

	# Check remaining digits 
	while (i < n) : 
		if (num[i] == "0") : 
			return True
		i = i + 1

	return False
	

# Driver Method 
num1 = "01023"
if(check_duck(num1)) : 
	print ("It is a duck number")
else : 
	print ("It is not a duck number")

# Write Python3 code here 
