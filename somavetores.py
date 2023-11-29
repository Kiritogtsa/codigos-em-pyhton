def inicio():
    matrix=[]
    tamanho=int(input("digite o tamanho do dois vetores: "))
    for x in range(2):
         vetor=[]
         if x<2 and x>0:
            print("mudou")
         for i in range(tamanho):
                vetor.append(int(input("digite o numero: ")))
         matrix.append(vetor)
    vetor=matrix[0]+matrix[1]
    print(vetor)
    soma=0
    for i in vetor:
        soma+=i
    print(soma)
inicio()
