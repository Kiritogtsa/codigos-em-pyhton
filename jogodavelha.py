class jogo:
    jogadorvercedor=""
    def __init__(self):
        self.tabuleiro=self.matrix()
        self.jogadoratula="x"
        teste=self.inicio()
    def inicio(self):
        while True:
            if self.verificar():
                print(f"{self.jogadorvercedor} venceu o jogo")
                return
            else:
                self.draw(self.tabuleiro)
                self.jogada()
    def draw(self,a):
        for i in a:
            print(i)
    def matrix(self):
        vetor=[]
        for i in range(3):
            x=[]
            for j in range(3):
               x.append("")
            vetor.append(x)
        return vetor 
    def jogada(self):
        self.jogadoratula
        self.movimento1=int(input("digite o numero da coluna: "))
        self.movimento2=int(input("digite o numero da linha: "))
        
        if self.verificartabuleiro(self.movimento1,self.movimento2):
            self.tabuleiro[self.movimento1][self.movimento2]=self.jogadoratula
            if self.jogadoratula=="x":
                self.jogadoratula="o"
            elif self.jogadoratula=="o":
                self.jogadoratula="x"
        else:
            print("posiçao ocupada")
    def verificartabuleiro(self,a,b):
        if self.tabuleiro[a][b]!="":
            return False
        return True
    def verificar(self):
        for i in range(3):
            if self.tabuleiro[i][0] == self.jogadoratula and self.tabuleiro[i][1] == self.jogadoratula and self.tabuleiro[i][2] == self.jogadoratula:
                self.jogadorvercedor=self.jogadoratula
                return True

        for i in range(3):
            if self.tabuleiro[0][i] == self.jogadoratula and self.tabuleiro[1][i] == self.jogadoratula and self.tabuleiro[2][i] == self.jogadoratula:
                self.jogadorvercedor=self.jogadoratula
                return True

        if self.tabuleiro[0][0] == self.jogadoratula and self.tabuleiro[1][1] == self.jogadoratula and self.tabuleiro[2][2] == self.jogadoratula:
            self.jogadorvercedor=self.jogadoratula
            return True

        if self.tabuleiro[2][0] == self.jogadoratula and self.tabuleiro[1][1] == self.jogadoratula and self.tabuleiro[0][2] == self.jogadoratula:
            self.jogadorvercedor=self.jogadoratula
            return True

        return False

teste=jogo()