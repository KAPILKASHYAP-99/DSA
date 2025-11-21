# chapter - 3 Formatted String in python

# topic - 1 . 3 formatted

name = "ABC"

course = "Python Course"

s = "Welcome %s to the %s"%(name,course)
print(s)
print()
###########
# using format function

s = "welcome {0} to the {1}".format(name,course)
print(s)
print()
############################
# using f-string

s = f"welcome {name} to the {course}"
print(s)
print()


