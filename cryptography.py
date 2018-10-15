"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

end = "false"
while end == "false":
    stringInt = []
    keyInt = []
    encryptedNumbers = []
    encryptedLetters = ""
    cyphertextNums = []
    cypherkeyNums = []
    decryptedNums = []
    decryptedLetters = ""
    userinput = input("Type e to encrypt, d to decrypt, or q to quit: ")
    if userinput != "e" and userinput != "d" and userinput != "q":
        print("Did not understand command, try again. ")
    elif userinput == "e":
        userString = input("Message: ")
        userKey = input("Key: ")
        for i in userString:
            stringInt.append(associations.find(i))
        for e in userKey:
            keyInt.append(associations.find(e))
        while len(keyInt) <= len(stringInt):
            keyInt = keyInt + keyInt
        zippedNumbers = zip(stringInt, keyInt)
        for p in zippedNumbers:
            encryptedNumbers.append((p[0] + p[1]))
        for t in encryptedNumbers:
            if t > 85:
                t = t - 85
            encryptedLetters = encryptedLetters + associations[t]
        print(encryptedLetters) 
    elif userinput == "d":
        userCyphertext = input("Message: ")
        cyphertextKey = input("Key: ")
        for q in userCyphertext:
            cyphertextNums.append(associations.find(q))
        for y in cyphertextKey:
            cypherkeyNums.append(associations.find(y))
        while len(cyphertextNums) >= len(cypherkeyNums):
            cypherkeyNums = cypherkeyNums + cypherkeyNums
        zippedCypher = zip(cyphertextNums, cypherkeyNums)
        for r in zippedCypher:
            decryptedNums.append((r[0] - r[1]))
        for h in decryptedNums:
            if h < 0:
                h = h + 85
            decryptedLetters = decryptedLetters + associations[h]
        print(decryptedLetters)
    elif userinput == "q":
        print("Better luck next time")
        end = "true"    
    