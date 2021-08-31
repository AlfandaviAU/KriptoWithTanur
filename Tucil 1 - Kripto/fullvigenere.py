from basicOps import *

plaintext = "Semburan lumpur panas di desa Porong, Sidoarjo, Jawa Timur belum juga berakhir."
input_key = "langitbiru"

# print(plaintext)
# print(input_key)

def encryptFullVigenere(text,key):
    arr_text = convertPlainToArr(text)
    arr_key = convertPlainToArr(generateKey(text,key))
    arr_hasil = []
    for i in range (len(text)):
        num_text = convertCharToNumExt(arr_text[i])
        # print("num"+str(num_text))
        num_key = convertCharToNumExt(arr_key[i])
        # print("key"+str(num_key))
        process = ((num_text + num_key ) % 256)
        res_char = hex(process)
        # print("process"+str(hex(process)))
        arr_hasil.append(res_char+",")
    return convertArrToPlain(arr_hasil)

def decryptFullVigenere(plaintext,text,key):
    arr_text = text.split(",")
    arr_key = convertPlainToArr(generateKey(text,key))
    arr_hasil = []
    for i in range (len(plaintext)-1):
        num_text = arr_text[i]
        # print(num_text)
        num_key = convertCharToNumExt(arr_key[i])
        process = (((int(num_text,16)) - num_key) % 256)
        # print(process)
        res_char = convertNumToCharExt(process)
        arr_hasil.append(res_char)
    return convertArrToPlain(arr_hasil)

# print(encryptFullVigenere(plaintext,input_key))
# print(decryptFullVigenere(plaintext,encryptFullVigenere(plaintext,input_key),input_key))

# asu = "0xbf,0xc6,0xdb,0xc9,0xde,0xe6,0xc3,0xd7,0x92,0xe1,0xe1,0xce,0xde,0xdc,0xdb,0x94,0xd2,0xca,0xe0,0xd6,0xdf,0x81,0xd2,0xd0,0x89,0xd8,0xc7,0xdc,0xd3,0x95,0xbc,0xd0,0xe0,0xd6,0xd7,0xdb,0x8e,0x89,0xc5,0xde,0xd0,0xd0,0xcf,0xd9,0xd3,0xe3,0x8e,0x89,0xbc,0xd6,0xe3,0xc2,0x8e,0xbb,0xd2,0xe1,0xd7,0xdb,0x92,0xd7,0xd1,0xcd,0xe3,0xd4,0x89,0xde,0xd7,0xd0,0xd3,0x95,0xce,0xc6,0xe0,0xc8,0xd4,0xdc,0xcb,0xdb,0xa0,"
# print(decryptFullVigenere(plaintext,asu,input_key))
# newarr = asu.split(",")
# print((newarr[78]))
# print(len(plaintext))
# print(convertPlainToArr(plaintext))
# print(convertArrToPlain(generateKey(plaintext,input_key)))
# print(convertArrToPlain(convertPlainToArr(plaintext)))



# print(convertPlainToArr(plaintext),generateKey(plaintext,input_key))