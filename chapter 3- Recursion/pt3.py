# topic - print 1 to N using Recursion in python 
# i/p : n = 4
# o/p : 1 2 3 4
# i/p : n = 5
# o/p : 1 2 3 4 5
# def print1toN(n):
#     if n == 0:
#         return
#     print1toN(n-1)
#     print(n)

# print1toN(3)

# topic - 2 print N to 1 using Recursion in python
# i/p : n = 5
# o/p : 5 4 3 2 1
# i/p : n = 2
# o/p : 2 1
def printNto1(n):
    if n <= 0:
        return
    print(n)
    printNto1(n-1)

n = 3
printNto1(n)