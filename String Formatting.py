
def print_formatted(number):
    # your code goes here
    l = len(bin(number)[2:])  # length of number in binary format as binary form has biggest length
            #  [2:] is used for eliminating the starting 0x,0b,0o from the converted numbers
    for i in range(1,number+1):
        print(str(i).rjust(l," "),end=" ")   # rjust is used for adjusting to right, end= " " keepas thge output in same line
        print(oct(i)[2:].rjust(l," "),end=" ")
        print(hex(i)[2:].upper().rjust(l," "),end=" ")    #  .upper() method used in case of hexadecimal as we need uppercase letters
        print(bin(i)[2:].rjust(l," "),end=" ")
        print()
        
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
    
