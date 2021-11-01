import sys

while True:
    S = sys.stdin.readline().strip("\n")
    if S == ".":
        break
    isvalid = True
    stack = []
    answer = 0
    for s in S:
        if s == "(" or s == "[":
            stack.append(s)
        elif (s == ")" or s == "]") and not stack:
            isvalid = False
            break
        elif s == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                isvalid = False
                break

        elif s == "]":
            if stack[-1] == "[":
                stack.pop()
            else:
                isvalid = False
                break
    if isvalid and not stack:
        print("yes")
    else:
        print("no")
