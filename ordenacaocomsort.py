def inicio():
    lista=[]
    tamanho=int(input("digite o tamanho da lista"))
    for i in range(tamanho):
        lista.append(int(input("digite um numero aqui")))
    print(lista)
    lista.sort()
    print(lista)
inicio()