while(True):
    a = input("no")
    try:
        a=int(a)
        if (a > 3):
            print("whatever")

    except Exception as e:
        print("your no is error")
        break

    except ValueError as e:
        print("you have given a wrong value") #you can raise many error that has been there in the python documentation

    print("Thanks for using this code") #the code will continue to this line even if exception occourd
#Note: we can also use custom error using "raise" syntax









