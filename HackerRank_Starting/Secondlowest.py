arr = []
for _ in range(int(input())):
        name = input("your name:")
        score = float(input("your grade:"))
        arr.append([name, score])

print(arr)
grade=[student[1] for student in arr]
student_name={student[1]:student[0] for student in arr}
grade.sort()


lowest=min(grade)
#print(lowest)
c=grade.count(lowest)
#print(c)
for i in range(c):
        grade.remove(lowest)
print(grade)


second_lowest_grade=grade[0]

second_lowest_grade_list=[]
for student in arr:
        if student[1]==second_lowest_grade:
                second_lowest_grade_list.append(student)

#Or els ewe can do
# Second_lowest_grade_list=[student for student in arr if student[1]==second_lowest_grade]

second_lowest_grade_list.sort()
for student in second_lowest_grade_list:
        print(student[0])




