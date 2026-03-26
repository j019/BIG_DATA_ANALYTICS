per=int(input("Enter Percentage: "))
if per>90:
    print("Grade A")
elif per>80 and per<=90:
    print("Grade B")
elif per>=60 and per<=80:
    print("Grade C")
else:
    print("Grade D")
