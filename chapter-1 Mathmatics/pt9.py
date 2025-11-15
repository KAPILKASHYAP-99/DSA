# chapter - All Divisors of a number
# input: n = 10
# output : 1 2 5 10

# input : n = 100
# output :  1 2 4 5 10 20 25 50 100

# input : n = 125
# output :  1 5 25 125

def printDivisors1(n):
    i = 1
    while (i*i<=n):
        if(n%i==0):
            print(i)
            if(i!=n/i):
                print(int(n/i))

        i += 1

def printDivisors2(n):
    i = 1
    while(i*i<n):
        if(n%i==0):
            print(i)
        i += 1

    while(i>=1):
        if(n%i==0):
            print(int(n/i)) 
        i -= 1

n = 15
printDivisors1(n)
printDivisors2(n)

