from basicOps import *

plainteks = cleanInput("temui ibu nanti malam")
huruf_ambil = "j"
kata_ingat = "JALAN GANESHA SEPULUH"
# asumsi huruf dipilih j dan akan diganti dengan i apabila ada j
separator = "x"
# print(len(plainteks))
def encryptPlayFair(bigram,matrix):
    hasil_akhir = []
    res_arr = [[]] * len(bigram)
    for i in range (len(bigram)):
        temp_arr = [[]]* 2
        for j in range (2):
            for k in range (len(matrix)):
                for l in range (len(matrix)):
                    if (bigram[i][j] == matrix[k][l]):
                        temp1 = k
                        temp2 = l
            temp_arr[j] = [temp1,temp2]
        # if (temp_arr[0][1] == temp_arr[1][1]):
        #     if (temp_arr[0][0] == 4):
        #         temp_arr[0][0] = 0
        #     else:
        #         temp_arr[0][0] += 1
        #     if (temp_arr[1][1] == 4):
        #         temp_arr[1][1] = 0
        #     else:
        #         temp_arr[1][0] += 1

    #     print(temp_arr)
    # print("Bigram after")
    for i in range (len(bigram)):
        temp_arr = [[]]* 2
        for j in range (2):
            for k in range (len(matrix)):
                for l in range (len(matrix)):
                    if (bigram[i][j] == matrix[k][l]):
                        temp1 = k
                        temp2 = l
            temp_arr[j] = [temp1,temp2]

        if (temp_arr[0][1] == temp_arr[1][1]): # VERTIKAL SAMA
            if (temp_arr[0][0] == 4):
                temp_arr[0][0] = 0
            else:
                temp_arr[0][0] += 1
            if (temp_arr[1][0] == 4):
                temp_arr[1][0] = 0
            else:
                temp_arr[1][0] += 1

        if (temp_arr[0][0] == temp_arr[1][0]): # HORIZONTAL SAMA
            if (temp_arr[0][1] == 4):
                temp_arr[0][1] = 0
            else:
                temp_arr[0][1] += 1
            if (temp_arr[1][1] == 4):
                temp_arr[1][1] = 0
            else:
                temp_arr[1][1] += 1

        if ((temp_arr[0][0] != temp_arr[1][0]) and (temp_arr[0][1] != temp_arr[1][1])): # DIAGONAL SAMA
            temp = temp_arr[0][1]
            temp_arr[0][1] = temp_arr[1][1]
            temp_arr[1][1] = temp
        res2 = []
        for idx in range (len(temp_arr)):
            res2.append(matrix[temp_arr[idx][0]][temp_arr[idx][1]])
        n = 2
        res = []
        for i in range (len(res2)-1):
            bentar = []            
            bentar.append(matrix[temp_arr[i][0]][temp_arr[i][1]] + matrix[temp_arr[i+1][0]][temp_arr[i+1][1]])
            res.append((bentar))
        hasil_akhir.append(res[0][0])
        # for i in range (len(res2)):
        # print(res[0][0],end=" ")
        # res = convertArrToPlain(res2)
        # res3 = [res[i:i+n] for i in range(0, len(res), n)]
        # print(res3)
        # print(temp_arr)
    return convertArrToPlainv2(hasil_akhir)

def decodePlayFair(text,matrix):
    hasil = []
    arr_text = (convertPlainToArrv2(text))
    for i in range (len(arr_text)):
        temp_arr = [[]]* 2
        for j in range (2):
            for k in range (len(matrix)):
                for l in range (len(matrix)):
                    if (arr_text[i][j] == matrix[k][l]):
                        temp1 = k
                        temp2 = l
            temp_arr[j] = [temp1,temp2]

        # print(temp_arr)
        if (temp_arr[0][1] == temp_arr[1][1]): # VERTIKAL SAMA
            if (temp_arr[0][0] == 0):
                temp_arr[0][0] = 4
            else:
                temp_arr[0][0] -= 1
            if (temp_arr[1][0] == 0):
                temp_arr[1][0] = 4
            else:
                temp_arr[1][0] -= 1

        if (temp_arr[0][0] == temp_arr[1][0]): # HORIZONTAL SAMA
            if (temp_arr[0][1] == 0):
                temp_arr[0][1] = 4
            else:
                temp_arr[0][1] -= 1
            if (temp_arr[1][1] == 0):
                temp_arr[1][1] = 4
            else:
                temp_arr[1][1] -= 1

        if ((temp_arr[0][0] != temp_arr[1][0]) and (temp_arr[0][1] != temp_arr[1][1])): # DIAGONAL SAMA
            temp = temp_arr[0][1]
            temp_arr[0][1] = temp_arr[1][1]
            temp_arr[1][1] = temp
        hasil.append(temp_arr)
        # print(temp_arr)
        # print(temp_arr[0])
        # print(matrix[temp_arr[i][j]][temp_arr[i][j+1]])
    # print(hasil)
    # print(hasil[0])
    # print(hasil[0][0])
    # print(matrix[hasil[0][0][0]][hasil[0][0][1]])
    # print(matrix[hasil[0][1][0]][hasil[0][1][1]])
    # print(matrix[hasil[1][0][0]][hasil[1][0][1]])
    # print(matrix[hasil[1][1][0]][hasil[1][1][1]])
    # print(matrix[hasil[2][0][0]][hasil[2][0][1]])
    # print(matrix[hasil[2][1][0]][hasil[2][1][1]])
    # print(matrix[hasil[3][0][0]][hasil[3][0][1]])
    # print(matrix[hasil[3][1][0]][hasil[3][1][1]])
    hasil2 = []
    for i in range (len(hasil)):
        for j in range (2):
            hasil2.append(matrix[hasil[i][j][0]][hasil[i][j][1]])
    for i in range (len(hasil2)):
        if hasil2[i] == "x":
            hasil2[i] = " "

    return(convertArrToPlain(hasil2))
        

if (validasiSeparator(plainteks,separator) == True): # Ketika separator valid
    # print("Matriksnya : ")
    matrix = generateKeySquare(kata_ingat,huruf_ambil)
    # print("Bigramnya awal")
    bigram = generateBigram(plainteks,separator)
    # print(bigram)
    print(encryptPlayFair(bigram,matrix))
    print(decodePlayFair(encryptPlayFair(bigram,matrix),matrix))

else:
    print("ravalid")