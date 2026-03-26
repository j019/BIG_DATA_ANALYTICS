str = input("Enter String: ")

reversed_str = ""

for i in range(len(str) - 1, -1, -1):
    reversed_str += str[i]

print("Reversed String:", reversed_str)


"""
empty=' '
for i in str:
    empty=i+empty
print(empty)
"""