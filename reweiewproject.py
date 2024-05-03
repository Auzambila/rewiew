from math import factorial
n=4
l=0,1
nu=1/30
a=3
s=0
k=0
for i in range(0,n):
    s+=a**i/(factorial(i))
P0=1/(s+a**n/(factorial(n)*(1-a/n)))
k=0
print(f"P0{P0}")
for k in range(1,11):
    if k<=n:
        Pk=P0*a**k/factorial(k)
        print(f"P{k}={Pk}")
        if k==4:
            print(f"Lq= {Pk*a*n/(n-a)**2}")
    elif k>n:
        Pk=P0*a**k/(factorial(n)*n**(k-n))
        print(f"P{k}={Pk}")
    
    

    
