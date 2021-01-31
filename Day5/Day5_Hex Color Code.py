# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())

for i in range(N):
    m = re.findall(r'(?!^)#([a-f0-9]{6}|[a-f0-9]{3})[^\n]', input(), re.IGNORECASE)
    if m:
        for s in m:
            print ('#' + s)