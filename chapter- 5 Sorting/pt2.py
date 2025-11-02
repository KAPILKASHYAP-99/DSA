#  1) sorting user defined using key-fun
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

# def myFun(p):
#     return p.x

# l = [Point(1,15),Point(10,5),Point(3,8)]
# l.sort(key=myFun)
# for i in l:
#     print(i.x,i.y)

# 2 Sorting user defined using __it__1
# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __lt__(self, other):
#         return self.x < other.x


# l = [Point(1, 15), Point(10, 5), Point(5, 8)]
# l.sort()

# for i in l:
#     print(i.x, i.y)


# 3 sorting user defined using __it__ method -2
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):

        if self.x == other.x:
            return self.y < other.y
        else:
            return self.x < other.x


l = [Point(1, 15), Point(10, 5), Point(1, 8)]
l.sort()

for i in l:
    print(i.x, i.y)
