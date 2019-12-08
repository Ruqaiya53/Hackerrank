if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total_marks = 0
    if query_name in student_marks:
        marks = student_marks.get(query_name)
        for i in marks:
            total_marks +=i
        total_percent = total_marks/3
        print("{:.2f}".format(total_percent))

    else:
        print("no value present")
        
