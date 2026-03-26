# Nested Loop

no = int(input("Enter number of lines: "))

"""
for i in range(1,no+1):
    for k in range(i):
        print(k+1 ," ",end=" ")
    print()
"""

for i in range(1,no+1):
    for sp in range(no,i,-1):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")
    print()


