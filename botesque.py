__author__ = 'KG'
mol = "\033[1mMol: \033[0m"
print(mol + "Hello.")
immData = "" # Immediate data
prevData = "" # Previous data
flags = ["1", "2"] # 1 = greeting, # 2 = farewell
flagData = ["Hi.", "Bye."]
while (immData != "Done." and immData != "Finished." and immData != "End."):
    immData = input("Response: ")
    immLen = len(immData)
    if immLen == 0:
        print(mol + "Please say something. If you're done, say \"Done\".")
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
        print(mol + "Oh okay. " + prevData)
    elif immData == "That is a farewell." or immData == "That's a farewell.":
        flags.extend("2")
        flagData.append(prevData)
        print(mol + "Oh okay.")
    index = 0
    for x in flagData:
        if (x == immData):
            if (flags[index] == "1"):
                print(mol + (flagData[index])[:(len(flagData[index]) - 1)] + " to you too.")
            if (flags[index] == "2"):
                print(mol + flagData[index])
                immData = "Done."
        index += 1
    prevData = immData
