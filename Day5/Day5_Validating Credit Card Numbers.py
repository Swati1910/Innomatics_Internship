# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())):
    N = input().strip()
    m = re.search(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$',N)
    if m:
        processed_string = "".join(m.group(0).split('-'))
        if bool(re.search(r'(\d)\1{3,}',processed_string)):
            print('Invalid')
        else:
            print('Valid')
    else:
        print('Invalid')