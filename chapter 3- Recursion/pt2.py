# practice for recursion (part1)
# problem 1
# def fun(n):
#     if n == 0:
#         return
#     print(n)
#     fun(n-1)
#     print(n)

# fun(3)

# problem 2
# def fun(n):
#     if n == 0:
#         return
#     fun(n-1)
#     print(n)
#     fun(n-1)

# fun(3)

# practice for recursion partn-2
# problem - 1
# def fun(n):
#     if n <= 1:
#         return 0
#     else:
#         return 1 + fun(n/2)

# fun(16)
# print(fun(16))  
# problem - 2
def fun(n):
    if n == 0:
        return
    fun(n//2)
    print(n % 2)

fun(13)