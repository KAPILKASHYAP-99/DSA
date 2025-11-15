# chapter - Prime Factorization
def isPrime(x):
    for i in range(2,x):
        if x % i == 0:
            return False

    return True

def printPFactor(n):
    for i in range(2,n+1):
        if isPrime(i):
            x = i
            while n % x == 0:
                print(i)
                x = x * i

n = int(input("enter n: \n"))
printPFactor(n)