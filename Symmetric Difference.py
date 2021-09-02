
# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
n = set(map(int,input().split()))
x = int(input())
y = set(map(int,input().split()))

draken = sorted(list(n.symmetric_difference(y)))
for i in draken:
    print(i)
    
