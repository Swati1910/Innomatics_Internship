# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())

set1 = map(int, input().split())
set1 = sorted(set1)

for i in range(len(set1)):
    if(i != len(set1)-1):
        if(set1[i]!=set1[i-1] and set1[i]!=set1[i+1]):
            print(set1[i])
            break;
    else:
        print(set1[i])
