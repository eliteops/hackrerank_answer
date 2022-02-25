if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()   # *line is used to take multiple arguments
        scores = list(map(float, line)) # now data is converted to float and then list
        student_marks[name] = scores
    query_name = input()
    marks = 0
    for i in student_marks[query_name]:
        marks = marks + i
    average = marks / 3
    print('%.2f'%average)               # %.2f is used to take only two digit after decimal in float
