from basicOps import *
from vigenere import encryptVigenere,decryptVigenere

plaintext = cleanInput("Semburan lumpur panas di desa Porong, Sidoarjo, Jawa Timur belum juga berakhir.")
input_key = cleanInput("langitbiru")
# print(len(input_key))

def encryptSuperEncryption(text,key):
    arr = (encryptVigenere(plaintext,input_key))
    # print(convertPlainToArr(arr))
    matrix = [["0" for i in range (len(input_key))]for j in range (len(input_key))]
    matrix2 = [["0" for i in range (len(input_key))]for j in range (len(input_key))]
    # asumsi dummy 0
    idx1 = 0
    idx2 = 0
    for i in range (len(arr)):
        matrix[idx1][idx2] = arr[i]
        idx2 += 1
        if (idx2 == 10):
            idx2 =  0
            idx1 += 1


    # for i in range (10):
    #         for j in range (10):
    #             print(matrix[i][j],end="")
    #         print("\n")


    arr_hasil = []
    for i in range (len(matrix)):
        for j in range (len(matrix)):
            matrix2[i][j] = matrix[j][i]
    # print("asu")
    # for i in range (10):
    #         for j in range (10):
    #             print(matrix2[i][j],end="")
    #         print("\n")

    for i in range (len(matrix2)):
        for j in range (len(matrix2)):
            arr_hasil.append(matrix2[i][j])

    return convertArrToPlain(arr_hasil)

def decryptSuperEncriptions(text,key):
    arr = convertPlainToArr(text)
    matrix = [["0" for i in range (len(input_key))]for j in range (len(input_key))]
    matrix2 = [["0" for i in range (len(input_key))]for j in range (len(input_key))]
    idx1 = 0
    idx2 = 0
    for i in range (len(arr)):
        matrix[idx1][idx2] = arr[i]
        idx2 += 1
        if (idx2 == 10):
            idx2 =  0
            idx1 += 1
    arr_hasil = []
    for i in range (len(matrix)):
        for j in range (len(matrix)):
            matrix2[i][j] = matrix[j][i]

    for i in range (len(matrix2)):
        for j in range (len(matrix2)):
            if (matrix2[i][j]!= "0"): # remove dummy
                arr_hasil.append(matrix2[i][j])
    # print(arr_hasil)
    return decryptVigenere(convertArrToPlain(arr_hasil),key)

# print(encryptSuperEncryption(plaintext,input_key))
# print(decryptSuperEncriptions(encryptSuperEncryption(plaintext,input_key),input_key))