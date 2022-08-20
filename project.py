n = int(input("Enter number of students: "))
student = {}
for i in range(n):
    name = input("Enter student's name")
    marks = int(input("Enter student's salary "))
    student[name] = marks
sort_st = sorted(student.values())
student1 = {}
for i in sort_st:
    for k in student.keys():
        if student[k] == i:
            student1[k] = i
            break
print(student1)
lis = [500, 300, 100]
price = {}
i = 0
for x in student1.keys():
    if i < 3:
        price[x] = lis[i]
        i = i+1

    else:
        break

print(price)

for x in student1.keys():
    if student1[x] >= 950:
        print("Congratulations ", x)
