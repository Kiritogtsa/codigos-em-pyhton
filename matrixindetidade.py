def inicio(ordem):
    matrix=[[0 for i in range(ordem)]for j in range(ordem)]
    for i in range(ordem):
        for j in range(ordem):
            if i==j :
                matrix[i][j]=1
    return matrix
teste=inicio(4)
for i in range(4):
    print(teste[i])

    