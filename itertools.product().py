
# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product   #  importing product from itertools as asked in the problem statement

funk = map(int,input().split())   #  taking input and splitting according to whitespace as there are more than 1 numbers
funk1 = map(int,input().split())  
draken = tuple(product(funk,funk1))    #  product finds the cartesian product and is stored as an object, so converted to tuple

for i in draken:
    print(i,end=" ")   #  we have to print individual elements of the tuplle
    
    
