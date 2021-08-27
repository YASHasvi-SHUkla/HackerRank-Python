
if __name__ == '__main__':
    s = input()
                  # different functions are created as we have to check if any character of string matches 
def fun1(s):      # function for checking alphanumeric
    for i in s:
        if i.isalnum():
            return True
            break
    return False
def fun2(s):      # function for checking alphabetic
    for i in s:
        if i.isalpha():
            return True
            break
    return False
def fun3(s):     # function for checking the digit
    for i in s:
        if i.isdigit():
            return True
            break
    return False
def fun4(s):     # function for checking lower case
    for i in s:
        if i.islower():
            return True
            break
    return False
def fun5(s):     # function for checking upper case
    for i in s:
        if i.isupper():
            return True
            break
    return False

  
alphanum = fun1(s)
alphabetic = fun2(s)     #  calling all the functions as they are required and are returning 
digit = fun3(s)
lower = fun4(s)
upper = fun5(s)

print(alphanum)
print(alphabetic)
print(digit)
print(lower)
print(upper)



