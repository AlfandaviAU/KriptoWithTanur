import math
# BASIC OPERASI YG DIPERLUKAN

def convertPlainToArr(text):
    list_text = list(text)
    arr = []
    for i in range (len(list_text)):
        arr.append(list_text[i])
    return arr

def convertPlainToArrv2(text):
    arr = text.split(' ')
    return arr


def convertArrToPlain(arr):
    return "".join(arr)

def convertArrToPlainv2(arr):
    return " ".join(arr)
# BIKIN KEY BERSAMBUNG 

def generateKey(text,key):
    arr_text = convertPlainToArr(text)
    arr_key = convertPlainToArr(key)
    index = 0

    for i in range(len(text)-len(arr_key)):
        if (index == len(arr_key)):
            index = 0
        arr_key.append(arr_key[index])
        # print(arr_key[index])
        # print(arr_key)
        index+=1
    return arr_key

def generateAutoKey(text,key):
    arr_text = convertPlainToArr(text)
    arr_key = convertPlainToArr(key)
    index = 0

    for i in range(len(text)-len(arr_key)):
        if (index == len(arr_text)):
            index = 0
        arr_key.append(arr_text[index])
        # print(arr_key[index])
        # print(arr_key)
        index+=1
    return arr_key


# CONVERT BIASA
def convertCharToNum(char):
    return ord(char)-96

def convertNumToChar(num):
    return chr(num+96)

def convertCharToNumExt(char):
    return ord(char)

def convertNumToCharExt(num):
    return chr(num)

# MEMBERSIHKAN INPUTAN
def cleanInput(text):
    return (convertArrToPlain(list(filter(lambda x: x.isalpha(), text.lower()))))



# print(generateAutoKey(convertPlainToArr("negarapenghasilminyak"),convertPlainToArr("indo")))
# print(convertNumToCharExt(33))


# PLAYFAIR
def validasiSeparator(text,separator):
    for i in range (len(text)-1):
        # print("i")
        if (text[i] == text[i+1]):
            if (text[i] == separator):
                return False
            else:
                return True
        else:
            return True


def generateBigram(plaintext,separator):
    text = convertPlainToArr(plaintext)
    for i in range (len(text)-1):
        if (text[i] == text[i+1]):
            text.insert(i+1,separator)

    if (len(text)% 2 != 0):
        text.insert(len(text),separator)
    arr = [[]] * int(math.ceil(len(text) / 2))
    panjang_text = len(text)
    index = 0
    for i in range (int(math.ceil(panjang_text / 2))):
        arr[i] = [text[index],text[index+1]]
        index += 2
        # if (panjang_text % 2 != 0 and (index+1 == panjang_text)):
        #     arr[i] = [text[index],separator]
        # else:
        #     arr[i] = [text[index],text[index+1]]
    return arr
    print(arr)

def generateKeySquare(text,huruf_ambil):
    arr = convertPlainToArr(cleanInput(text))
    if (huruf_ambil in arr):
        arr.remove(huruf_ambil)
    
    new_arr = list(dict.fromkeys(arr))

    alphabet = []
    for i in range (1,27):
        alphabet.append(convertNumToChar(i))
    
    for i in range (len(new_arr)):
        alphabet.remove(new_arr[i])

    if (huruf_ambil in alphabet):
        alphabet.remove(huruf_ambil)
    # print(new_arr)
    # print(alphabet)
    matrix = [[0 for i in range (5)]for j in range (5)]
    idx1 = 0
    idx2 = 0
    for i in range (len(new_arr)):
        matrix[idx1][idx2] = new_arr[i]
        idx2 += 1
        if (idx2 == 5):
            idx2 =  0
            idx1 += 1
        # print(idx1, idx2)
        

    for i in range (len(alphabet)):
        matrix[idx1][idx2] = alphabet[i]
        idx2 += 1
        if (idx2 == 5):
            idx2 =  0
            idx1 += 1
        if (idx1 == 5):
            break
        # print(idx1, idx2)
        
    return matrix
    # matrix[5][0] = "a"
    for i in range (5):
        for j in range (5):
            print(matrix[i][j],end="")
        print("\n")



# generateKeySquare("JALAN GANESHA SEPULUH","j")
# # print(convertPlainToArr(cleanInput("temui ibu nanti malam")))
# generateBigram(convertPlainToArr(cleanInput("temui ibu nanti malam")),"x")

# arr = [[]] * int(math.ceil(len(text) / 2))
# arr[0] = [text[0],text[1]]
# arr[1] = [text[2],text[3]]
# print(arr)