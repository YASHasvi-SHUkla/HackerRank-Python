
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split()) # this will store all the numbers in the form of list
    
    print(hash(tuple(integer_list)))  # tuple converts the list into list and then hash does it's job.
    
    
