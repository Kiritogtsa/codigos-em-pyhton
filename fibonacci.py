def inicio():
    x=[0,1,0]
    tamanho=int(input("digite o tamanho do fibonacci, no caso ate que tamanho a sequencia vai"))
    for i in range(1,tamanho+1):
        print(f"{i} --> {x[1]}")
        x[0]=x[1]
        x[1]=x[2]+x[1]
        x[2]=x[0]
inicio()