marks1=int(input("Enter Marks for first subject: "))
marks2=int(input("Enter Marks for second subject: "))
marks3=int(input("Enter Marks for third subject: "))
average = (marks1+marks2+marks3)/3
match average:
    case average if average > 90:
        print("Distinction.")
    case average if average>60 and average<=90:
        print("First Class.")
    case average if average >= 33 and average<=60:
        print("Second class.")
    case average if average < 33:
        print("Fail.")
    case _:
        print("Invalid Input")
