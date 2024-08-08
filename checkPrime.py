def checkPrime(n):
    if n==1:
        print("Neither prime nor composite")
        return

    for i in range (2,n//2): 
        if n%i==0:
            print("Not a prime")
            return
    print("Prime")

checkPrime(n = int(input()))