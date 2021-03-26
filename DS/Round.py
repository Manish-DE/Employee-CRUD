# Python3 code to round the given 
# integer to a whole number 
# which ends with zero.
# function to round the number
def round(n):
	# Smaller multiple
	a = (n // 10) * 10
	# Larger multiple
	b = a + 10
	if ( n -a > b - n):
        return b
    else:
        return a
	# Return of closest of two
	#return (b if n - a > b - n else a)
# driver code
n = 4728
print(round(n))

# This code is contributed by "Sharad_Bhardwaj".
