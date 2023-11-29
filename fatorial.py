def inicio():
    numero=int(input("digite o numero que vc quer saver o fatorial"))
    soma=1
    for i in range(1,numero+1):
        soma*=i
    print(soma)
inicio()
