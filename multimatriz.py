def mult(a):
    soma=1
    for i in a:
        for j in i:
            soma*=j
    return soma
def inicio():
    matrix=[]
    for i in range(2):
        vetor=[]
        for j in range(2):
            vetor.append(int(input("digite um valor: ")))
        matrix.append(vetor)
    rels=mult(matrix)
    print(rels)
    print(matrix)
inicio()