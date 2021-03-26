def fixArray(ar, n):
    for i in range(n):
        for j in range(i,n):
            if(i == ar[j]):
                ar[i],ar[j] = ar[j],ar[i]
                break;
        if(i != ar[i]):
            ar[i] =-1
    for i in range(n):
        print(ar[i], end = " ")

ar = [ -1, -1, 6, 1, 9, 3, 2, -1, 4, -1 ]
n = len(ar)
fixArray(ar, n);
