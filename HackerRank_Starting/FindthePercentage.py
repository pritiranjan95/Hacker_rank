# arr=[]
# for i in range(int(input())):
#     name=input("name of the student:")
#     for i in range(3):
#         marks=int(input(f"mark of the {name}: "))
#         b= name, arr.append([marks])
#     print(b)


 # bapi [23, 34, 34]
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    # print(name)
    # print(*line)
    scores = list(map(float, line))
    # print(scores)
    student_marks[name] = scores
print(student_marks)
query_name = input()

a=student_marks[query_name]
print(a)
per=sum(a)/len(a)
print("%.2f" % per)



