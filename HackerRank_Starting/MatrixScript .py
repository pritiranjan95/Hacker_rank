#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
matrix=list(zip(*matrix))
print(matrix)
s=''
for i in matrix:
    s=s+"".join(i)
search=re.sub(r'[^a-zA-Z0-9@]+(?=\w)',' ',s)
# search=re.sub(r'\b[^a-zA-Z0-9]+\b',' ',s)
print(search)
