# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
setM = set(map(int, input().split()))
N = int(input())
setN = set(map(int, input().split()))

DiffM = setM.difference(setN)
DiffN = setN.difference(setM)

output = DiffM.union(DiffN)

for i in sorted(list(output)):
    print(i)
