# Python program to check if a string 
# is Pangrammatic Lipogram 

# collection of letters 
alphabets = 'abcdefghijklmnopqrstuvwxyz'

#''' 
#Category			 No of letters unmatched 
#Pangram					 0 
#Lipogram				 >1 
#Pangrammatic Lipogram	 1 
#'''

# function to check for a Pangrammatic Lipogram 
def panLipogramChecker(s): 
	s.lower() 
	
	# variable to keep count of all the letters 
	# not found in the string 
	counter = 0
	
	# traverses the string for every 
	# letter of the alphabet 
	for ch in alphabets: 
		# character not found in string then increment count 
		if(s.find(ch) < 0): 
			counter += 1

	if(counter == 0): 
		result = "Pangram"
	elif(counter == 1): 
		result = "Pangrammatic Lipogram"
	else: 
		result = "Not a pangram but might a lipogram"

	return result 

# Driver program to test above function 
def main(): 
	print(panLipogramChecker("The quick brown fox \ jumped over the lazy dog")) 
	
	print(panLipogramChecker("The quick brown fox \ jumps over the lazy dog")) 

	print(panLipogramChecker("The quick brown fox jum\ over the lazy dog")) 
	

if __name__ == '__main__': 
	main() 
