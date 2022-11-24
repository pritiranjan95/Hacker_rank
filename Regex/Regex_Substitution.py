import re
n=int(input())
for _ in range(n):
    text=input()
    s=re.sub(r"(?<=\s)&&(?=\s)",'and',text)
    s=re.sub(r"(?<=\s)\|\|(?=\s)", 'or', s)
    print(s)
