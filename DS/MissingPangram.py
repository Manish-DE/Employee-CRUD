MAX_CHAR = 26
def missingchar(str):
    present = [False for i in range(MAX_CHAR)]
    for i in range(len(str)):
        if(str[i].lower() >= 'a' and str[i].lower() <= 'z'):
            present[ord(str[i]) - ord('a')] =True
    res = ""
    for i in range(MAX_CHAR):
        if(present[i]==False):
            res += chr(i+ord('a'))
    return res

Str = "The brown for jumps over the dog"
print(missingchar(Str))