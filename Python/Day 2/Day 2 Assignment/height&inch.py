height = int(input("Enter Height in cm: "))



feetdivision = height//30.48
feetmodulus = height/30.48
inch= ((feetmodulus - feetdivision)*30.48)/2.54


print("Height in feet :",feetdivision," and inches : ",inch)
