# topic - tower of hanoi in python

def THO(n,A,B,C):
    if n == 1:
        print("Move 1 from",A,"to",C)
    else:
        THO(n-1,A,C,B)
        print("MOVE",n,"from",A,"to",C)
        THO(n-1,B,A,C)

THO(3,'A','B','C')