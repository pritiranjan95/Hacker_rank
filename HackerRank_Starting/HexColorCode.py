# c= "adaddad"
# for i in c:
#     print(i)
import re
is_css=False
css=False
n=int(input())
for _ in range(n):
    line=input("Css code here:")
    if '{' in line:
        # css=True
        s = re.findall("#[a-fA-F 0-9]{3,6}", line)
        for i in range(len(s)):
            print(s[i])
    # elif '}' in line:
    #     css=False
    # elif css:
    #     # s=re.findall("^#[a-fA-F 0-9]{3,6}", line)
    #     # for i in range(len(s)):
    #     #     print(s[i])

