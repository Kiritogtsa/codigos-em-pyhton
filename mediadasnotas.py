def calculo(a):
    media=a
    soma=0
    for x in media:
        soma+=x
    return soma/len(a)
def inicio():
    alunos=[]
    media=[]
    tamanho=int(input("digite quantos alunos tem: "))
    for i in range(tamanho):
         notas=[]
         for j in range(3):
            notas.append(int(input("digite a nota do aluno")))
         print("outro aluno")
         alunos.append(notas)
         media.append(calculo(alunos[i]))
    print(media)
inicio()
                


