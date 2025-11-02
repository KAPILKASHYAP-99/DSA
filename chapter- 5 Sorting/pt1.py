# 1 list
# l1 = [5,10,15,1]
# l1.sort()
# print(l1)

# l2 = [1,5,3,10]
# l2.sort(reverse=True)
# print(l2)

# l3 = ["gfg","ide","courses"]
# l3.sort()
# print(l3)

def myFun(s):
    return len(s)

l = ['gfg','courses','python']
l.sort(key=myFun)
print(l)

l.sort(key=myFun,reverse=True)
print(l)


