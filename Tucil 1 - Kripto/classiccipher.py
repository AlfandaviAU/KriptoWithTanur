import re
import random
from fullviginerekey import fullViginereKeyMatrix
alphabetRegex = re.compile("[^a-zA-Z]")



# Appending key until length bigger or equal with sourcetext length
def keyExpand(key : str, sourcelength : int) -> str:
    expandedKey = key
    while len(expandedKey) < sourcelength:
        expandedKey += key
    return expandedKey

def fullViginereKeygen() -> "26x26 char matrix":
    key = []
    alphabet = [chr(0x41+i) for i in range(26)]
    while len(key) != 26:
        alpha = []
        while len(alpha) != 26:
            randpick = random.choice(alphabet)
            if randpick not in alpha:
                alpha.append(randpick)
        key.append(alpha)
    return key

def playfairStrToKey(keysrc : str) -> "5x5 char matrix":
    playfairKey = []
    for i in range(5):
        playfairKey.append([c.upper() for c in keysrc[i*5:(i+1)*5]])
    return playfairKey

def alphabetSanitize(text : str) -> str:
    sanitizedText = text
    alphabetRegex.sub("", sanitizedText)
    return sanitizedText.replace(" ", "")


# Standard Viginere Cipher
# ASCII in hex A-Z, 0x41 - 0x5A
def viginere(sourcetext : str, key : str, encrypt = True) -> str:
    resulttext = ""

    alphabetRegex.sub("", sourcetext)
    sourcetext = sourcetext.upper()
    key        = key.upper()
    key        = keyExpand(key, len(sourcetext))

    for i in range(len(sourcetext)):
        if encrypt:
            vigishift = ord(sourcetext[i]) + ord(key[i]) - 0x41
            if vigishift > 0x5A:
                vigishift -= 26
        else:
            vigishift = ord(sourcetext[i]) - ord(key[i]) + 0x41
            if vigishift < 0x41:
                vigishift += 26
        resulttext += chr(vigishift)

    return resulttext



# Full Viginere Cipher
def fullViginere(sourcetext : str, key : str, encrypt = True) -> str:
    resulttext = ""

    alphabetRegex.sub("", sourcetext)
    sourcetext = sourcetext.upper()
    key        = key.upper()
    key        = keyExpand(key, len(sourcetext))

    subTable = fullViginereKeyMatrix
    for i in range(len(sourcetext)):
        if encrypt:
            row    = ord(key[i]) - 0x41
            column = ord(sourcetext[i]) - 0x41
            resulttext += subTable[row][column]
        else:
            column = ord(sourcetext[i]) - 0x41
            rowSub = subTable[ord(key[i]) - 0x41]
            for j in range(len(rowSub)):
                if rowSub[j] == sourcetext[i]:
                    resulttext += chr(j + 0x41)

    return resulttext



# Auto Key Viginere Cipher
def autoKeyViginere(sourcetext : str, key : str, encrypt = True) -> str:
    resulttext = ""

    alphabetRegex.sub("", sourcetext)
    sourcetext = sourcetext.upper()
    key        = key.upper()

    if len(key) < len(sourcetext) and encrypt:
        key += sourcetext

    for i in range(len(sourcetext)):
        if encrypt:
            vigishift = ord(sourcetext[i]) + ord(key[i]) - 0x41
            if vigishift > 0x5A:
                vigishift -= 26
        else:
            vigishift = ord(sourcetext[i]) - ord(key[i]) + 0x41
            if vigishift < 0x41:
                vigishift += 26
            key += chr(vigishift)
        resulttext += chr(vigishift)

    return resulttext



# Extended Viginere Cipher
def extendedViginere(sourcetext : str, key : str, encrypt = True) -> str:
    resulttext = []

    key = keyExpand(key, len(sourcetext))
    for i in range(len(sourcetext)):
        if encrypt:
            vigishift = ord(sourcetext[i]) + ord(key[i])
            if vigishift > 0xFF:
                vigishift -= 0xFF
        else:
            vigishift = ord(sourcetext[i]) - ord(key[i])
            if vigishift < 0:
                vigishift += 0xFF
        resulttext.append(str(vigishift) + " ")

    return resulttext











# Playfair Cipher
def playfair(sourcetext : str, key : "5x5 int matrix", encrypt = True, useSpaceSeparator = False) -> str:
    sourcetext = sourcetext.upper().replace("J", "I").replace(" ", "")
    alphabetRegex.sub("", sourcetext)

    # Generating character pair
    i = 0
    charPair = []
    while i < len(sourcetext):
        newEntry = None
        if i == len(sourcetext) - 1:
            newEntry = (sourcetext[i], "X")
        elif sourcetext[i] == sourcetext[i+1]:
            newEntry = (sourcetext[i], "X")
            i -= 1
        else:
            newEntry = (sourcetext[i], sourcetext[i+1])
        charPair.append(newEntry)
        i += 2

    # Generating key matrix index
    charIndexes = [None for i in range(26)]
    for i in range(5):
        for j in range(5):
            charIndexes[ord(key[i][j]) - 0x41] = {"row" : i, "column" : j}

    resulttext = ""
    if encrypt:
        for pair in charPair:
            firstCharIdx  = charIndexes[ord(pair[0]) - 0x41]
            secondCharIdx = charIndexes[ord(pair[1]) - 0x41]

            if firstCharIdx["row"] == secondCharIdx["row"]:
                rowKey       = key[firstCharIdx["row"]]
                resulttext  += rowKey[(firstCharIdx["column"] + 1) % 5]
                resulttext  += rowKey[(secondCharIdx["column"] + 1) % 5]
            elif firstCharIdx["column"] == secondCharIdx["column"]:
                columnKey    = [key[i][firstCharIdx["column"]] for i in range(5)]
                resulttext  += columnKey[(firstCharIdx["row"] + 1) % 5]
                resulttext  += columnKey[(secondCharIdx["row"] + 1) % 5]
            else:
                resulttext  += key[firstCharIdx["row"]][secondCharIdx["column"]]
                resulttext  += key[secondCharIdx["row"]][firstCharIdx["column"]]

            if useSpaceSeparator:
                resulttext += " "
    else:
        for pair in charPair:
            firstCharIdx  = charIndexes[ord(pair[0]) - 0x41]
            secondCharIdx = charIndexes[ord(pair[1]) - 0x41]

            if firstCharIdx["row"] == secondCharIdx["row"]:
                rowKey       = key[firstCharIdx["row"]]
                resulttext  += rowKey[(firstCharIdx["column"] - 1) % 5]
                resulttext  += rowKey[(secondCharIdx["column"] - 1) % 5]
            elif firstCharIdx["column"] == secondCharIdx["column"]:
                columnKey    = [key[i][firstCharIdx["column"]] for i in range(5)]
                resulttext  += columnKey[(firstCharIdx["row"] - 1) % 5]
                resulttext  += columnKey[(secondCharIdx["row"] - 1) % 5]
            else:
                resulttext  += key[firstCharIdx["row"]][secondCharIdx["column"]]
                resulttext  += key[secondCharIdx["row"]][firstCharIdx["column"]]

                if useSpaceSeparator:
                    resulttext += " "

    return resulttext



# Ring Z26 inverse
z26Inverse = [
    1, None, 9, None, 21,
    None, 15, None, 3, None,
    19, None, None, None, 7,
    None, 23, None, 11, None,
    5, None, 17, None, 25,
    None
    ]

# Affine cipher
# key[0] is m, not m inverse
def affineCipher(sourcetext : str, key : (int, int), encrypt = True) -> str:
    assert key[0] != 13 and key[0] % 2 == 1 and 0 < key[0] < 26
    sourcetext = sourcetext.upper().replace(" ", "")

    resulttext = ""
    if encrypt:
        for char in sourcetext:
            resulttext += chr((key[0] * (ord(char) - 0x41) + key[1]) % 26 + 0x41)
    else:
        mInverse = z26Inverse[key[0]-1]
        for char in sourcetext:
            resulttext += chr((mInverse * ((ord(char) - 0x41) - key[1])) % 26 + 0x41)

    return resulttext



# Playfair testing
# sampleMtxPlyf = [
#     ["A", "L", "N", "G", "E"],
#     ["S", "H", "P", "U", "B"],
#     ["C", "D", "F", "I", "K"],
#     ["M", "O", "Q", "R", "T"],
#     ["V", "W", "X", "Y", "Z"]
#     ]
# ALNGESHPUBCDFIKMOQRTVWXYZ


# print(playfair("temui ibu nanti malam", sampleMtxPlyf))
# print(playfair("ZBRSFYKUPGLGRKVSNLQV", sampleMtxPlyf, False))
