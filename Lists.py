
if __name__ == '__main__':
    N = int(input())
    yashasvi = [] 
    
    for i in range(0,N):
        draken = input().split() # input is being split on the basis of space as multiple input's is required for "insert".
        if draken[0] == "print":
            print(yashasvi)
        elif draken[0] == "insert":
            yashasvi.insert(int(draken[1]),int(draken[2])) # input is being explicitly converted into int type as we require a integer.
        elif draken[0] == "remove":
            yashasvi.remove(int(draken[1]))
        elif draken[0] == "append":
            yashasvi.append(int(draken[1]))
        elif draken[0] == "pop":
            yashasvi.pop()
        elif draken[0] == "sort":
            yashasvi.sort()
        else:
            yashasvi.reverse()
       
      
