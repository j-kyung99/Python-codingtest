def solution(n, lost, reserve):
    answer = 0
    student = [1] * n
    for i in reserve:
        student[i-1] = 2
    for i in lost:
        if student[i-1] == 2:
            student[i-1] = 1
        else:
            student[i-1] = 0
    for i in range(n-1):
        if student[i] == 2 and student[i+1] == 0:
            student[i] -= 1
            student[i+1] += 1
        elif student[i] == 0 and student[i+1] == 2:
            student[i] += 1
            student[i+1] -= 1
    return n - student.count(0)