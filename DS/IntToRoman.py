class Solutaion(object):
    def intToRoman(self, num):
        number = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        sym = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"] 
        i = len(number)-1
        while num:
            div = num // number[i]
            num %= number[i]
            while div:
                print(sym[i], end= "")
                div -= 1;
            i -= 1
roman = Solutaion()
roman.intToRoman(3912)   

    

   