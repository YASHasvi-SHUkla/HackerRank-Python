
# Enter your code here. Read input from STDIN. Print output to STDOUT
test = int(input())

for i in range(0,test):
    a = int(input())
    s1 = set(map(int,input().split()))
    b = int(input())
    s2 = set(map(int,input().split()))
    print(s1.issubset(s2))
    
