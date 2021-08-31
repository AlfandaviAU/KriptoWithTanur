mtx1 = [[17,17,5],[21,18,21],[2,2,19]]
mtx2 = [[15],[0],[24]]


mtx3 = [[0 for i in range(len(mtx2[0]))]for j in range (len(mtx1[1]))]
print(mtx3)
print(len(mtx1[1]))
print(len(mtx2[0]))
for i in range (len(mtx1)):
    for j in range (len(mtx2[0])):
        for k in range (len(mtx2)):
            mtx3[i][j] += mtx1[i][k] * mtx2[k][j]

print(mtx3)