n = int(input("Enter The Number of units: "))
charge = 0
bill = 0
i=0
while i<=n:
    if i==101:
        charge = 5
    elif i==201:
        charge = 10

    bill+=charge
    i+=1

print("units :",n," bill: ",bill)
