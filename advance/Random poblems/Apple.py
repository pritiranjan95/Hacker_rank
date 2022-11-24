try:
    n=int(input("how many apple do I have?"))
    mx=int(input("What us the maximum range of students?"))
    mn=int(input('What is teh minimum range of students?'))


    if mn==mx:
        print("this is not a range")
        quit()

    for i in range(mn,mx+1):
        if n%i==0:
            print(f"the no {i} is a divisor")
        else:
            print(f"{i} is not a divisor")
except:
    print("invalid input")






