__author__ = 'KG'
print("Hello.")
immData = "" # Immediate data
while (immData != "Done."):
    immData = input("Response: ")
    immLen = len(immData)
    if immLen == 0:
        print("Please say something. If you're done, say \"Done\".")
    while immData[0] == " " and immLen > 0:
        immData = immData[1:]
        immLen -= 1
    while immData[immLen - 1] == " " and immLen > 0:
        immData = immData[:(immLen - 1)]
        immLen -= 1
    if immData[0].islower():
        immData = immData.capitalize()
    if immData[immLen - 1] != "." and immData[immLen - 1] != "!" and immData[immLen - 1] != "?":
        immData += "."
    print(immData)
    print()
