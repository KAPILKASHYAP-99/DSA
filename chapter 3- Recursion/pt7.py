# topic palindrome check using recursion
# i/p : abbcbba
# o/p : yes
# i/p : abba
# o/p : yes
# i/p: geeks
# o/p : no

# a recursive python program
# to check wheather a given 
# number is palindrome or not
def isPalRec(st,s,e):
    if (s == e):
        return True
    if (st[s] != st[e]):
        return False
    if (s < e + 1):
        return isPalRec(st, s+ 1, e - 1);
    return True
def isPalindrome(st):
    n = len(st)
    if (n == 0):
        return True
    return isPalRec(st,0,n-1);
st = "geeg"
if (isPalindrome(st)):
    print("yes")
else:
    print("No")


