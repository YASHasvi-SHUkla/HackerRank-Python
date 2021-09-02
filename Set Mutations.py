
# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
s = set(map(int,input().split()))
n = int(input())

for i in range(n):
    draken = input().split() 
    if draken[0] == "intersection_update":
        funk = set(map(int,input().split()))    #  every time new set is inputted
        s.intersection_update(funk)
    elif draken[0] == "update":
        funk = set(map(int,input().split()))
        s.update(funk)
    elif draken[0] == "symmetric_difference_update":
        funk = set(map(int,input().split()))
        s.symmetric_difference_update(funk)
    else:
        funk = set(map(int,input().split()))
        s.difference_update(funk)
print(sum(s))
