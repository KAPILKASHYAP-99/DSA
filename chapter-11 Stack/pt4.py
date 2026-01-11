# check for balanced parenthesis in python


def isMatching(a, b):
    if (a == "(" and b == ")") or (a == "{" and b == "}") or (a == "[" and b == "]"):
        return True
    else:
        return False


def isBalanced(exper):
    stack = []
    for x in exper:
        if x in ("(", "{", "["):
            stack.append(x)
        elif x in (")", "}", "]"):
            if not stack:
                return False
            elif isMatching(stack[-1], x) == False:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True


a = input("Enter expression: ")

print(isBalanced(a))

a = input("Enter expression: ")

print(isBalanced(a))
