import re
n=int(input())
for _ in range(n):
    card_no=input()
    print(len(card_no))
    if len(card_no)==16 or len(card_no)==19:
        if re.search(r"(^[456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})",card_no):
            if not re.search(r"(\d)\1{3}", card_no.replace("-", '')):
                print("Valid")
            else:
                print("Invalid1")
        else:
            print("Invalid2")

    else:
        print("Invalid3")
