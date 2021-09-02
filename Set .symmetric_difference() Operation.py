
# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
n = set(map(int,input().split()))
x = int(input())
y = set(map(int,input().split()))

draken = n.symmetric_difference(y)
print(len(draken))
