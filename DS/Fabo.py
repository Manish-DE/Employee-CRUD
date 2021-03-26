def fabo(n):
    if n < 0:
        print("incorrect")
    elif n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fabo(n-1) + fabo(n-2)

def faboprint(n):
    
    f1 = 0
    f2 = 1
    if n < 1:
        return
    print(f1, end = " ")
    for x in range(1,n):
        print(f2, end = " ")
        next = f1 + f2
        f1= f2
        f2= next

print(fabo(3))
faboprint(3)
