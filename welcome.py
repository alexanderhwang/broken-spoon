__author__ = 'KG'

hello = "Hello world."
print(hello)
count = 0
while (count < len(hello)):
    print(hello[count])
    count += 1


print()
val = len(hello)

print(val)

print()
val *= len(hello)
val += val
val *= val

print(val)
print(str(val) + " + " + str(val * 2) + " = " + str(val * 3))
print()

data = input("Enter something: ")

if len(data) > 0 and data.isalpha() and data != "no":
    print(data)
elif data == "no":
    print("")
else:
    print("no")
print()
