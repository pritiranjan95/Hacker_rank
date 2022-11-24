import re
# str = 'an example word:cat!!'
# match = re.search('example', str)
# # If-statement after search() tests if it succeeded
# if match:
#   print('found', match.group()) ## 'found word:cat'
# else:
#   print('did not find')
# str="pritiranjanpanda95@gmail.com"
# match = re.search('\w+@[\w.]+', str)
# if match:
#   print(match.group())  ## 'alice-b@google.com'

thousand = 'M{0,3}'
hundred = '(C[MD]|D?C{0,3})'
ten = '(X[CL]|L?X{0,3})'
digit = '(I[VX]|V?I{0,3})'

regex_pattern = r"M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$" # Do not delete 'r'.

import re
match=(re.match(regex_pattern, input()))
if match:
  print(True)
else:
  print(False)