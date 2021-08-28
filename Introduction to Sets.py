
def average(array):
    # your code goes here
    mikey = set()    #  creating an empty set
    for i in array:
        mikey.add(i)   #  adding all the elemets of the array into the set, so that they are all distinct
    draken = round(sum(mikey)/len(mikey),3)     #  rounding the average to three places after the decimal according to the question
    return draken

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
    
    
