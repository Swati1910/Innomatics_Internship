# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = '[qwrtypsdfghjklzxcvbnm]'
m = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(), re.I)
if m:
    for s in m:
        print (s) 
else:
    print (-1)
