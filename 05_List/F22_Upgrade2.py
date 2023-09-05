def nextGrade(grade):
    if grade == 'A':
        return 'A'
    if grade == 'F':
        return 'D'
    if len(grade) == 2:
        return chr(ord(grade[0]) - 1)
    return grade + "+"

def index_of(grades, ID):
    for i in range(len(grades)):
        if grades[i][0] == ID:
            return i
    return -1

def upgrade(grades, IDs):
    grades.sort()
    for i in range(len(grades)):
        if grades[i][0] in IDs:
            grades[i][1] = nextGrade(grades[i][1])

exec(input())
exec(input())
exec(input())
