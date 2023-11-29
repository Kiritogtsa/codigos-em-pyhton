def ordenacao(a):
    for i in range(1,len(a)):
        j=i
        while j>0 and a[j]<a[j-1]:
            a[j],a[j-1]=a[j-1],a[j]
            j-=1
    return a
def inicio():
    lista=[]
    tamanho=int(input("digite o tamanho da lista: "))
    for i in range(tamanho):
        lista.append(int(input("digite o numero aqui: ")))
    print(lista)
    lista=ordenacao(lista)
    print(lista)
inicio()