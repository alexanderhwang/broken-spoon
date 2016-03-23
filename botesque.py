__author__ = 'KG'
# Initial greeting needs work.

print("Hello.")
immData = "" # Immediate data
prevData = "" # Previous data
flags = ["1"] # 1 = greeting
flagData = ["Hi."]
while (immData != "Done." and immData != "Finished." and immData != "End."):
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
    if immData == "That is a greeting." or immData == "That's a greeting.":
        flags.extend("1")
        flagData.append(prevData)
    index = 0
    for x in flagData:
        if (x == immData):
            if (flags[index] == "1"):
                print((flagData[index])[:(len(prevData) - 1)] + " to you too.")
        index += 1
    prevData = immData
