def soma(a):
    rels=0
    for i in a:
        for j in i:
            print(j)
            rels+=j
    print(rels)
    
def inicio():
    matrix=[]
    for i in range(3):
        vetor=[]
        for j in range(3):
            vetor.append(int(input("digite um numero: ")))
        matrix.append(vetor)
    soma(matrix)
inicio()