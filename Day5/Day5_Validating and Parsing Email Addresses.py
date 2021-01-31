# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils 

N = int(input())

pattern = r'^[a-z][\w\-\.]+@[a-z]+\.[a-z]{1,3}$'
for i in range(N):
    result = email.utils.parseaddr(input())
    if re.search(pattern, result[1]):
        print(email.utils.formataddr(result)) 