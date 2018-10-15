"""
cryptography.py
Author: Joseph Goff
Credit: Morgan Gardner

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

end = "false"
while end == "false":
    stringint = []
    keyint = []
    encryptednumbers = []
    encryptedletters = ""
    cyphertextnumbers = []
    cypherkeynumbers = []
    decryptednumbers = []
    decryptedletters = ""
userinput = input("Type e to encrypt, d to decrypt, or x to exit: ")
    if userinput != "e" and userinput != "d" and userinput != "x":
        print("Invalid command. Please try again. ")
    elif userinput == "e":
        userstring = input("Message: ")
        userkey = input("Key: ")
        for s in userstring:
            stringint.append(associations.find(s))
        for a in userkey:
            keyint.append(associations.find(a))
        while len(keyint) <= len(stringint):
            keyint = keyint + keyint
        zippednumbers = zip(stringint, keyint)
        for d in zippednumbers:
            encryptednumbers.append((d[0] + d[1]))
        for r in encryptednumbers:
            if r > 46:
                r = r - 46
            encryptedletters = encryptedletters + associations[r]
        print(encryptedletters) 
    elif userinput == "d":
        usercyphertext = input("Message: ")
        cyphertextkey = input("Key: ")
        for y in usercyphertext:
            cyphertextnumbers.append(associations.find(y))
        for i in cyphertextkey:
            cypherkeynumbers.append(associations.find(i))
        while len(cyphertextnumbers) >= len(cypherkeynumbers):
            cypherkeynumbers = cypherkeynumbers + cypherkeynumbers
        zippedcypher = zip(cyphertextnumbers, cypherkeynumbers)
        for e in zippedcypher:
            decryptednumbers.append((e[0] - e[1]))
        for w in decryptednumbers:
            if w < 0:
                w = w + 46
            decryptedletters = decryptedletters + associations[w]
        print(decryptedletters)
    elif userinput == "x":
        print("You have exited.")
        end = "true"    
    