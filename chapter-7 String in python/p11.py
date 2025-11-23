# topic check if string is rotated

# 1 while loop
# s = input("Enter a String:\n")
# low = 0

# high = len(s)-1

# while low<high:
#     if s[low]!=s[high]:
#         print("No")
#         break
#     low = low+1
#     high = high-1
    
# else:
#     print("Yes")

# 2 String slicing
s = input("Enter a String:\n")

if s==s[::-1]:
    print("Yes")
else:
    print("No")