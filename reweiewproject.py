from math import factorial 
n=4 #надо разделить оператора и переменную пробелами
l=0,1 #надо разделить оператора и переменную пробелами
nu=1/30 #надо разделить оператора и переменную пробелами
a=3 #надо разделить оператора и переменную пробелами
s=0 #надо разделить оператора и переменную пробелами
k=0 #надо разделить оператора и переменную пробелами
for i in range(0,n):
    s+=a**i/(factorial(i)) #надо разделить оператора и переменную пробелами
P0=1/(s+a**n/(factorial(n)*(1-a/n))) #надо разделить оператора и переменную пробелами
k=0 # надо разделить оператора и переменную пробелами
print(f"P0{P0}")
for k in range(1,11):
    if k<=n: # надо разделить оператора и переменную пробелами
        Pk=P0*a**k/factorial(k) # надо разделить оператора и переменную пробелами
        print(f"P{k}={Pk}") # надо разделить оператора и переменную пробелами
        if k==4: # надо разделить оператора и переменную пробелами
            print(f"Lq= {Pk*a*n/(n-a)**2}") # надо разделить оператора и переменную пробелами
    elif k>n: # надо разделить оператора и переменную пробелами
        Pk=P0*a**k/(factorial(n)*n**(k-n)) # надо разделить оператора и переменную пробелами
        print(f"P{k}={Pk}") # надо разделить оператора и переменную пробелами
    
    

    
