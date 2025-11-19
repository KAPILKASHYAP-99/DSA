# chapter - Distinct Element in a list
#  1 ) I/p : l = [10,20,10,30,30,20]
# o/p : 3

# 2) I/P : L = [10,10,10]
# O/P : 1

# I/P : L = [10,20,30]
# O/P : 3
  
l = [10,20,10,30,30,20]

def cDistinct(l):
    return len(set(l))

print(cDistinct(l))

