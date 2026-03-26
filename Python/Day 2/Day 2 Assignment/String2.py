str1 = input("Enter String: ")
str2=''
if len(str1)< 2:
    print(str2)
else:
    s=str1[:2]+str1[-2:]
    print(s)
