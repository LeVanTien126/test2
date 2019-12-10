import numpy as np

std_gpa = {}

#Enter some new items (key, value) to the dictionary
std_gpa['Hai'] = 7.0
std_gpa['Viet'] = 4.0
std_gpa['Thu'] = 5.0
std_gpa['Hoang'] = 8.5
std_gpa['Nam'] = 6.5
std_gpa['Tram'] = 5.5
std_gpa['Minh'] = 9.5
std_gpa['Tuan'] = 1.5
std_gpa['Thanh'] = 6.5
print()

#Print all items of the dictionary
print('Students: ', std_gpa, '\n')

print('a. Student Distinction:')
count1 = 0
for name, gpa in std_gpa.items():
    if gpa > 8.0:
        print(name, 'GPA',gpa)
        count1 +=1
print()

print('b. Student Merit:')
count2 = 0
for name, gpa in std_gpa.items():
    if 6.5 < gpa <= 8.0:
        print(name, 'GPA',gpa)
        count2 +=1
print()

print('c. Student Pass:')
count3 = 0
for name, gpa in std_gpa.items():
    if 4.0 <= gpa <= 6.5:
        print(name, 'GPA',gpa)
        count3 +=1
print()

print('d. Student Failed:')
count4 = 0
for name, gpa in std_gpa.items():
    if gpa < 4.0:
        print(name, 'GPA',gpa)
        count4 +=1
print()

print('e.')
print('Number of Distionsion Students:',count1)
print('Number of Merit Students:',count2)
print('Number of Pass Students:',count3)
print('Number of Failed Students:',count4)
print()

print('f.')
pass_rate = (count1 + count2 + count3) / (count1 + count2 + count3 + count4) * 100
print('Pass rate:',round(pass_rate, 2), '%')
if pass_rate > 30:
    print('Successful Semester!')
else:
    print('Unsuccessful Semester!')