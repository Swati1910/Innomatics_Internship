# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = input()
set1=set(input().split(" "))
n2= input()
set2=set(input().split(" "))
set3=set1.intersection(set2)
print (len(set3))
