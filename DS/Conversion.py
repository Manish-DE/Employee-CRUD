
def conversion(str2,str1):
    res = ""
    for i in str1:
        if(str2.find(i)  > 0):
            res += chr(ord('a') + str2.find(i))
        else:
            return "Invalid String"
    return res
  
charSet= "qwertyuiopasdfghjklzxcvbnm"
str1 = "egrt"
print(conversion(charSet,str1))