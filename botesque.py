__author__ = 'KG'

# check other names, deal with confuse, fix name change

mol = "\033[1mMol: \033[0m"
print(mol + "Hello.")
immData = "" # Immediate data
prevData = "" # Previous data
response = False
confuse = False
flags = ["1", "1", "1", "1", "2", "2", "2"] # 1 = greeting, # 2 = farewell, # 3 = name
flagData = ["Greetings.", "Hi.", "Hello.", "Hey.", "Bye.", "Goodbye.", "Farewell."]
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
    immDataTemp = immData.lower()
    if "mol " in immDataTemp:
        valTemp = immDataTemp.find("mol ")
        immData = immData[:valTemp] + immData[(valTemp + 5):]
        immLen -= 4
    if " mol" in immDataTemp:
        valTemp = immDataTemp.find(" mol")
        immData = immData[:valTemp] + immData[(valTemp + 5):]
        immLen -= 4
    if ", mol" in immDataTemp:
        valTemp = immDataTemp.find(", mol")
        immData = immData[:valTemp] + immData[(valTemp + 5):]
        immLen -= 5
    if "mol, " in immDataTemp:
        valTemp = immDataTemp.find("mol, ")
        immData = immData[:valTemp] + immData[(valTemp + 5):]
        immLen -= 5
    if immData[0].islower():
        immData = immData[0].capitalize() + immData[1:]
    if immData[immLen - 1] != "." and immData[immLen - 1] != "!" and immData[immLen - 1] != "?":
        immData += "."
    print(immData)
    print()
    if immData == "That is a greeting." or immData == "That's a greeting." or immData == "That is a hello." or immData == "That's a hello." or immData == "That means hello." or immData == "That means hi.":
        flags.extend("1")
        flagData.append(prevData)
        response = True
        print(mol + "Oh okay. " + prevData)
    elif immData == "That is a farewell." or immData == "That's a farewell." or immData == "That is a goodbye." or immData == "That's a goodbye." or immData == "That means goodbye." or immData == "That means bye.":
        flags.extend("2")
        flagData.append(prevData)
        response = True
        print(mol + "Oh okay.")
    elif "My name is " in immData:
        responseA = "Oh okay. "
        index = 0
        for x in flagData:
            if x == immData:
                if (flags[index] == "3"):
                    flags.remove("3")
                    responseA = "Oh, I thought your name was " + flagData[index]
                    del flagData[index]
            index += 1
        flags.extend("3")
        flagData.append(immDataTemp[11:].capitalize())
        response = True
        print(mol + responseA + "I'll keep that in mind.")
    elif "My name's " in immData:
        responseA = "Oh okay. "
        index = 0
        for x in flagData:
            if x == immData:
                if (flags[index] == "3"):
                    flags.remove("3")
                    del flagData[index]
            index += 1
        flags.extend("3")
        flagData.append(immDataTemp[10:].capitalize())
        response = True
        print(mol + "Oh okay. I'll keep that in mind.")
    elif "Call me " in immData:
        responseA = "Oh okay. "
        index = 0
        for x in flagData:
            if x == immData:
                if (flags[index] == "3"):
                    flags.remove("3")
                    del flagData[index]
            index += 1
        flags.extend("3")
        flagData.append(immDataTemp[8:].capitalize())
        response = True
        print(mol + "Oh okay. I'll keep that in mind.")
    elif "I am " in immData:
        responseA = "Oh okay. "
        index = 0
        for x in flagData:
            if x == immData:
                if (flags[index] == "3"):
                    flags.remove("3")
                    del flagData[index]
            index += 1
        flags.extend("3")
        flagData.append(immDataTemp[5:].capitalize())
        response = True
        print(mol + "Oh okay. I'll keep that in mind.")
    elif "I'm " in immData:
        responseA = "Oh okay. "
        index = 0
        for x in flagData:
            if x == immData:
                if (flags[index] == "3"):
                    flags.remove("3")
                    del flagData[index]
            index += 1
        flags.extend("3")
        flagData.append(immDataTemp[4:].capitalize())
        response = True
        print(mol + "Oh okay. I'll keep that in mind.")
    elif "What's my name?" in immData or "what is my name?" in immData or "Who am I?" in immData:
        response = True
        name = ""
        index = 0
        for x in flags:
            if (x == "3"):
                name = flagData[index]
            index += 1
        if name != "":
            print(mol + "Your name is " + name + ".")
        else:
            print(mol + "I'm sorry, I don't know what your name is.")
    index = 0
    for x in flagData:
        if x == immData:
            if (flags[index] == "1"):
                response = True
                nameInsert = ""
                index2 = 0
                for y in flags:
                    if (y == "3"):
                        nameInsert = ", " + flagData[index2]
                    index2 += 1
                print(mol + (flagData[index])[:(len(flagData[index]) - 1)] + " to you too" + nameInsert + ".")
            if (flags[index] == "2"):
                response = True
                nameInsert = ""
                index2 = 0
                for y in flags:
                    if (y == "3"):
                        nameInsert = ", " + flagData[index2]
                    index2 += 1
                print(mol + (flagData[index])[:(len(flagData[index]) - 1)] + nameInsert + ".")
                immData = "Done."
        index += 1
    if (response == False):
        confuse = True
        print(mol + "Sorry, what?")
    prevData = immData
    response = False
