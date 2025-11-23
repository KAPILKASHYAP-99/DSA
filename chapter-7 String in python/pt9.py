# topic - Reverse a string in python
# 1 using for loop
s = input("Enter a String:\n")

rev = ""

for i in s:
    rev = i+rev

print(rev)

# 2 Slicing
s = input("Enter a String:\n")

print(s[::-1])