# chapter - Palindrome Number
def isPal(n):
    rev = 0
    temp = n
    while temp != 0:
        id = temp % 10
        rev = rev * 10 + id
        temp = temp // 10

    if (rev == n):
        print(True)
    else:
        print(False)

x = 789987
isPal(x)
    