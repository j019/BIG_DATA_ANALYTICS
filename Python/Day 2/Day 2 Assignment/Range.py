start = int(input("Enter start range : "))
end = int(input("Enter end range: "))
if start<end:
    if start%2!=0:
        for i in range(start,end,2):
            print(i)
    else:
        print("Enter odd number.")
else:
    print('Starting range is more than ending range')
