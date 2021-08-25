
def count_substring(string, sub_string):
    draken = 0
    for i in range(0,len(string)):
        
        if string[i:].startswith(sub_string):
            draken = draken + 1

    return draken

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
