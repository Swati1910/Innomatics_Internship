# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = int(input())
set1 = set(map(int, input().split()))
n2 = int(input())

for i in range(n2):
    (p, q)=input().split()
    set2 = set(map(int, input().split()))
    if p=='intersection_update':
        set1.intersection_update(set2)
    elif p=='update':
        set1.update(set2)
    elif p=='symmetric_difference_update':
        set1.symmetric_difference_update(set2)
    elif p=='difference_update':
        set1.difference_update(set2)
print (sum(set1))