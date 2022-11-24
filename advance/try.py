while(True):
    print("press q to quit")
    a = input("Enter a no")
    if a=="q":
        break
    try:
        a = int(a)
        if a > 6:
            print("you guessed it right")
    except Exception as e:
        print(f"your entered no is a error{e}")
        break





