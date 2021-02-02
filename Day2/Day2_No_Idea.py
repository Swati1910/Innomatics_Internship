# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = list(map(int,input().split()))
Arr = list(map(int,input().strip().split()))
A = set(map(int,input().strip().split()))
B = set(map(int,input().strip().split()))
count = 0

for i in Arr:
    if i in A:
        count += 1
    elif i in B:
        count -= 1
print(count)