import re
for i in range(int(input())):
    name = input()
    email = name.split()
    # x= name <email>
    a=re.match("^<[A-Za-z0-9][\w|\-|\.|\_]+@[A-Za-z]+\.[A-Za-z]{1,3}>$", email[1])
    if bool(a):
        print(name)
    else:
        print("no")

# import re
# name=input()
# x=re.match("^[A-aZ-z] [\w|.|-|_]", name)
# if x:
#     print("True")