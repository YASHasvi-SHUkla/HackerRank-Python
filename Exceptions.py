
for i in range(int(input())):
    a,b =input().split()
    try:
        print(int(a)//int(b))
    except ValueError as p:
        print("Error Code:",p)
    except ZeroDivisionError as e:
        print("Error Code:",e)
