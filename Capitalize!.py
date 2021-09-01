
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = " "+ s     #  adding a space at the starting of the string
    mikey = ""     # creating an empty string
    l = list(s)    # convertig string into list and storing it to l
    for i in range(0,len(l)):
        if l[i] == " ":
            l[i+1] = l[i+1].capitalize()    #  converting the next characater after every space into a uppercase
            mikey = mikey+l[i]       
        else:
            mikey = mikey + l[i]
    mikey = mikey[1:]            
    return mikey

  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

    
    
