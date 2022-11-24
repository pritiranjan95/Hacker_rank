import re
n=int(input("What's the time"))
for _ in range(n):
    no1=str(input("what's the no?"))
    x=re.search("^[789]\d{9}$", no1)
    if x:
        print("Yes")
    else:
        print("No")
#
# import re
# for i in range(int(input())):
#     print ('YES' if re.search(r"^[789]\d{9}$",input()) else 'NO')

