# Validating Postal Codes

import re
p=int(input())
for _ in range(p):
    p=input()
    s=(bool(re.search(r"^([1-9][0-9][0-9][0-9][0-9][0-9])$",p)) and len(re.findall(r"(\d)(?=\d\1)", p))>2)

    print(s)


