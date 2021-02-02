# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    n1 = input()
    set1=set(input().split(" "))
    n2= input()
    set2=set(input().split(" "))
    print (set1.issubset(set2))
