# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
from re import match
T = int(input())
for i in range (T):
    s = input()
    print(bool(re.match(r'^[+-]?\d*?\.{1}\d+$',s)))
    
    