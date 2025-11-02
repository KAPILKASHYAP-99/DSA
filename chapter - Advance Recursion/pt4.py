# Josephus Problem in python
# ip: n = 7 , k = 3
# op: 3
# i/p: n = 8 , k = 2
# o/p : 0
def jos(n,k):
    if n == 1:
        return 0
    else:
        return (jos(n-1,k) + k) % n

print(jos(8,2))    