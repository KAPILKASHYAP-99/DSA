# topic - writing base cases in recursion
#1) factorial n when n _> 0
# i/p: n = 4
# op: 24
# ip : n = 0
# op : 1
# 2) n-th fibonacii number where n_> 0
# ip: n = 4
# op: 3
# ip: n = 0
# op: 0

# program to print factorial of number
# recursively
def recursive_factorial(n):
    if n == 1 : # Base case
        return n
    
    else:
        return n * recursive_factorial(n-1)
    
num = 6
if num < 0:
    print("invalid input !")
elif num == 0:
    print(1)
else:
    print(recursive_factorial(num))


    

