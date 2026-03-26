print("""Road Tax Criteria:
      cost price > 100000 - 15%
      cost price > 50000 and <=100000 - 10%
      cost price <= 50000 - 5%""")


costprice=int(input("Enter cost Price: "))

if costprice>100000:
    print("Road tax on Bike: ",costprice*0.15)
elif costprice>50000 and costprice <=100000:
    print("Road tax on Bike: ",costprice*0.1)
else:
    print("Road tax on Bike: ",costprice*0.05)
