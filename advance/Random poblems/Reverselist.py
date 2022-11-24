list=[]
try:
    list.append(int(input("enter teh first no")))
    list.append(int(input("enter teh second no")))
    list.append(int(input("enter teh third no")))
    print(list)
except:
    print("Put integer only")
def formula1():
    list.reverse()
    print(f"the reverse is {list}")

def formula2():
    a= list[::-1]
    print(f"hey formula 2 lst {a}")

formula1()
formula2()
