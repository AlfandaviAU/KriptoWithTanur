from basicOps import *

# plaintext = cleanInput("Semburan lumpur panas di desa Porong, Sidoarjo, Jawa Timur belum juga berakhir.")
plaintext = cleanInput("Semburan lumpur panas di desa Porong, Sidoarjo, Jawa Timur belum juga berakhir.")
input_key = cleanInput("langitbiru")

# print(plaintext)
# print(input_key)

def encryptVigenere(text,key):
    arr_text = convertPlainToArr(text)
    arr_key = convertPlainToArr(generateKey(text,key))
    arr_hasil = []
    for i in range (len(text)):
        num_text = convertCharToNum(arr_text[i])
        num_key = convertCharToNum(arr_key[i])
        process = ((num_text + num_key - 2) % 26) + 1
        res_char = convertNumToChar(process)
        arr_hasil.append(res_char)
    return convertArrToPlain(arr_hasil)

def decryptVigenere(text,key):
    arr_text = convertPlainToArr(text)
    arr_key = convertPlainToArr(generateKey(text,key))
    arr_hasil = []
    for i in range (len(text)):
        num_text = convertCharToNum(arr_text[i])
        num_key = convertCharToNum(arr_key[i])
        process = ((num_text - num_key) % 26) + 1
        res_char = convertNumToChar(process)
        arr_hasil.append(res_char)
    return convertArrToPlain(arr_hasil)

# print(encryptVigenere(plaintext,input_key))
# print(decryptVigenere(encryptVigenere(plaintext,input_key),input_key))


# print(convertPlainToArr(plaintext))
# print(convertArrToPlain(generateKey(plaintext,input_key)))
# print(convertArrToPlain(convertPlainToArr(plaintext)))



# print(convertPlainToArr(plaintext),generateKey(plaintext,input_key))