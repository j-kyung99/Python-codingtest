def solution(board, moves):
    answer = 0
    moves = [i-1 for i in moves]
    stack = []
    for move in moves:
        for row in board:
            if row[move] != 0:
                stack.append(row[move])
                row[move] = 0
                break
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            answer += 2
            stack.pop()
            stack.pop()
                
    return answer