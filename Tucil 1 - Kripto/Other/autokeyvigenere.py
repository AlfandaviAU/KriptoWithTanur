from basicOps import *

plaintext = cleanInput("negarapenghasilminyak")
input_key = cleanInput("indo")

print(plaintext)
print(input_key)

def encryptAutoVigenere(text,key):
    arr_text = convertPlainToArr(text)
    arr_key = convertPlainToArr(generateAutoKey(text,key))
    arr_hasil = []
    for i in range (len(text)):
        num_text = convertCharToNum(arr_text[i])
        num_key = convertCharToNum(arr_key[i])
        process = ((num_text + num_key - 2) % 26) + 1
        res_char = convertNumToChar(process)
        arr_hasil.append(res_char)
    return convertArrToPlain(arr_hasil)

def decryptAutoVigenere(plaintext,text,key):
    arr_text = convertPlainToArr(text)
    arr_key = convertPlainToArr(generateAutoKey(plaintext,key))
    arr_hasil = []
    for i in range (len(text)):
        num_text = convertCharToNum(arr_text[i])
        num_key = convertCharToNum(arr_key[i])
        process = ((num_text - num_key) % 26) + 1
        res_char = convertNumToChar(process)
        arr_hasil.append(res_char)
    return convertArrToPlain(arr_hasil)

# print(encryptAutoVigenere(plaintext,input_key))
# print(decryptAutoVigenere(plaintext,encryptAutoVigenere(plaintext,input_key),input_key))


# print(convertPlainToArr(plaintext))
# print(convertArrToPlain(generateKey(plaintext,input_key)))
# print(convertArrToPlain(convertPlainToArr(plaintext)))



# print(convertPlainToArr(plaintext),generateKey(plaintext,input_key))