a = int(input("What is you age/year of birth"))
isYear=False
isAge=False

if a > 1900:
   isYear=True
else:
    isAge= True

if (a<1900 and isYear):
    print("It seems you are the oldest man alive.")
    exit()
if a>2022:
    print("You are not even born yet")
    exit()

if isAge:
    a=2022-a
print(f"you will be 100 year old in {a+100}")

interestedage=int(input("In which year you want to know your age?"))
print(f"you will be {interestedage-a} old on {interestedage}")







