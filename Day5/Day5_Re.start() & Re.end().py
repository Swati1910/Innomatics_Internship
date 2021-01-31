# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
k = input()
m = re.finditer(r'(?=(' + k + '))', s)
result = False
for i in m:
    result = True
    print((i.start(1), i.end(1) - 1))

if result == False:
    print((-1, -1))