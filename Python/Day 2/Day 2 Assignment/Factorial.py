n = int(input("Enter Number: "))

if n==0:
    print(1)
elif n==1:
    print(1)
elif n>1:
    fact=1
    i=1
    while i<=n:
        fact*=i
        i+=1
    print(fact)
else:
    print("Enter Positive value")
