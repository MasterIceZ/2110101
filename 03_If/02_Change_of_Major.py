'''
model student 
id gpax comprog cal1 cal2
'''

def gradeValid(student):
    if student[2] != 'A':
        return False
    if ord(student[3]) > ord('C'):
        return False
    if ord(student[4]) > ord('C'):
        return False
    return True

def getBetter(student_a, student_b):
    if not gradeValid(student_a):
        return student_b[0]
    if not gradeValid(student_b):
        return student_a[0]

    if float(student_a[1]) != float(student_b[1]):
        if float(student_a[1]) > float(student_b[1]):
            return student_a[0]
        else:
            return student_b[0]
    if student_a[3] != student_b[3]:
        if ord(student_a[3]) < ord(student_b[3]):
            return student_a[0]
        else:
            return student_b[0]
    if student_a[4] != student_b[4]:
        if ord(student_a[4]) < ord(student_b[4]):
            return student_a[0]
        else:
            return student_b[0]
    return "Both"


student_a = input().split()
student_b = input().split()

a_valid = gradeValid(student_a)
b_valid = gradeValid(student_b)

if not a_valid and not b_valid:
    print('None')
else:
    print(getBetter(student_a, student_b))
