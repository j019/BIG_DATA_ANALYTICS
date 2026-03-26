no = int(input("Enter n of lines: "))
count=1
for i in range(1,no+1):
    for k in range(0,i):
        print(count,end=" ")
        count+=1
    print()
