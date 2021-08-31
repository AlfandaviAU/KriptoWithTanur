from basicOps import *

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
    return gcd(a, b) == 1


def encryptAffine(pesan,a,b,geser):
    # a =  7
    # b =  26
    # geser = 10
    if (coprime(a,b) == True):
        # pesan = "kripto"
        arr = convertPlainToArr(pesan)
        arr2 = []
        for i in range (len(arr)):
            arr2.append(convertCharToNum(arr[i])-1)
        arr3 = []
        for i in range (len(arr2)):
            # print(arr2[i])
            # print(((a * arr2[i]) + geser))
            temp = ((a * arr2[i]) + geser) % 26
            # print(temp)
            arr3.append(convertNumToChar(temp+1))
        # print(arr2)
        return convertArrToPlain(arr3)
    else:
        return False

def decryptAffine(text,a,b,geser):
    if (coprime(a,b) == True):
        # pesan = "kripto"
        arr = convertPlainToArr(text)
        arr2 = []
        for i in range (len(arr)):
            arr2.append(convertCharToNum(arr[i])-1)
        arr3 = []
        for i in range (len(arr2)):
            c = pow(a,-1,b)
            # print(arr2[i])
            # print(((a * arr2[i]) + geser))
            temp = (c * (arr2[i] - geser)) % 26
            # print(temp)
            arr3.append(convertNumToChar(temp+1))
        # print(arr2)
        return convertArrToPlain(arr3)
    else:
        return False

print(encryptAffine("kripto",7,26,10))
print(decryptAffine(encryptAffine("kripto",7,26,10),7,26,10))