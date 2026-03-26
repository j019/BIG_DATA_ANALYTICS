no=int(input("Enter the number of lines: "))
for i in range(1,no+1):
    for sp in range(no,i,-1):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")
    print()
