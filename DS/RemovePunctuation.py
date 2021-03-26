
def removePunctuation(str):
    
    modifiedstr=""
    for i in str.lower():
        if(((ord('a') <= ord(i)) and (ord(i) <= ord('z'))) or ord(i) == ord(' ')):
            modifiedstr += i
        
    print(modifiedstr)


string = "Welcome???@@##$ to#$% Geeks%$^for$%^&Geeks"
removePunctuation(string) 

