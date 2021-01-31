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
string = ""      
for i in range(m):
    string += "".join(matrix[j][i] for j in range(n))
res = re.sub(r"(?<=\w)[!@#$%&\s]+(?=\w)",r" ",string)    
sys.stdout.write(res)
