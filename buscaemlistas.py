def inicio():
    numeros=[]
    tamanho=int(input("digite o tamanho da lista:"))
    for i in range(tamanho):
        numeros.append(int(input("digite o numero")))
    print(numeros)
    busca=int(input("digite o numero que vc quer achar a posiçao: "))
    soma=0
    for i in numeros:
        if busca==i:
            break
        soma+=1
    print(f"{soma} e a posicao do numero em espefico")
inicio()