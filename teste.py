def jogar():
    jogador_atual = "x"
    tabuleiro = [['', '', ''], ['', '', ''], ['', '', '']]

    while True:
        desenhar_tabuleiro(tabuleiro)

        if verificar_vitoria(tabuleiro):
            print(f"O jogador {jogador_atual} venceu!")
            break

        movimento_x, movimento_y = obter_movimento(jogador_atual,tabuleiro)
        colocar_símbolo(tabuleiro, movimento_x, movimento_y, jogador_atual)

        jogador_atual = "o" if jogador_atual == "x" else "x"


def desenhar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(linha)


def obter_movimento(jogador_atual,tabuleiro):
    while True:
        movimento_x = input("Digite a coluna (1-3): ")
        movimento_y = input("Digite a linha (1-3): ")

        movimento_x = int(movimento_x) - 1
        movimento_y = int(movimento_y) - 1

        if movimento_x < 0 or movimento_x > 2 or movimento_y < 0 or movimento_y > 2:
            print("Movimento inválido. Tente novamente.")
        elif tabuleiro[movimento_x][movimento_y] != "":
            print("Posição ocupada. Tente novamente.")
        else:
            return movimento_x, movimento_y


def colocar_símbolo(tabuleiro, movimento_x, movimento_y, jogador_atual):
    tabuleiro[movimento_x][movimento_y] = jogador_atual


def verificar_vitoria(tabuleiro):
    for linha in range(3):
        if tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] != "":
            return True

    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] != "":
            return True

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != "":
        return True

    if tabuleiro[2][0] == tabuleiro[1][1] == tabuleiro[0][2] != "":
        return True

    return False


jogar()
