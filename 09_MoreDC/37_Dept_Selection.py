n = int(input())

depts = dict()
students = list()
students_list = list()
student_depts = dict()

for i in range(n):
  line = input().split()
  depts[line[0]] = int(line[1])

m = int(input())
for i in range(m):
  line = input().split()
  students.append([float(line[1]), line[0], line[2], line[3], line[4], line[5]])
  students_list.append(line[0])

sorted_students = sorted(students, reverse=True)

for student in sorted_students:
  for dept in student[2:]:
    if depts[dept] == 0:
      continue
    depts[dept] -= 1
    student_depts[student[1]] = dept
    break

sorted_students_id = sorted(students_list)

for student in sorted_students_id:
  print(student, student_depts[student])