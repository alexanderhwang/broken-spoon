__author__ = 'KG'

hello = "Hello world."
print(hello)
count = 0
while (count < len(hello)):
    print(hello[count])
    count += 1


val = len(hello)

print(val)

val *= len(hello)
val += val
val *= val

print(val)
print(str(val) + " + " + str(val * 2) + " = " + str(val * 3))

