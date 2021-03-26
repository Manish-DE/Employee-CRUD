alphabets = 'abcdefghijklmnopqrstuvwxyz'

count = 0
def CheckPangram(s):
    for ch in alphabets:
        if (s.find(ch) < 0):
            count = count +1;
            return False
        else:
            return True


sentence = "The brown fox jumps over the little lazy dog"

if (CheckPangram(sentence)): 
	print ('"'+sentence+'"')
	print ("is a pangram")
else: 
	print ('"'+sentence+'"')
	print ("is not a pangram")
        