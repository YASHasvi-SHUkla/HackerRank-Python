
n = int(input())    # used for taking number of elements of set
s = set(map(int,input().split()))
mikey = int(input())      #  for taking the number of commands

for i in range(0,mikey):
    draken = input().split()    # taking commands as input one by one, splitting them as input is of more than one word/character
    if draken[0] == "discard":
        s.discard(int(draken[1]))   #  converting the second part of the input in integer as it is a number
    elif draken[0] == "pop":
        s.pop()
    else:
        s.remove(int(draken[1]))      #  same here as for remove
        
print(sum(list(s)))

