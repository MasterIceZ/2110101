f = open('data1.txt', 'r')

file_text = list()

for line in f:
  file_text.append(line)

print(file_text)