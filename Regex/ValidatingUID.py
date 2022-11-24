import re
n=int(input())
for _ in range(n):
    uid=input()
    if len(uid)==10:
        if re.search(r"[0-9]{3,}[a-zA-Z]{2,}", uid):
            if re.search(r'(a-zA-Z)\1', uid):
                print('Invalid1')
            else:
                print('Valid')
        else:
            print("Invalid3")
    else:
        print("Invalid4")


# u="abcdefaabbcd"
# s=re.search(r".*(.)\1.*",u)
# print(s)
