def solution(ingredient):
    answer = 0
    stack = []
    for plus in ingredient:
        stack.append(plus)
        if len(stack) >= 4 and stack[-4] == 1 and stack[-3] == 2 and stack[-2] == 3 and stack[-1] == 1:
            answer += 1
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
    return answer