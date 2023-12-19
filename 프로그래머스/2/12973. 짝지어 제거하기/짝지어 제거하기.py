def solution(s):
    stack = []
    for i in s:
        stack.append(i)
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
    return 1 if len(stack) == 0 else 0