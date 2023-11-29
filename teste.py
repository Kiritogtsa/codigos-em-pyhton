class JogoDaVelha:
  """
  Representa um jogo da velha.
  """

  def __init__(self):
    self.tabuleiro = self.matrix()
    self.jogadoratual = "X"

  def matrix(self):
    vetor = []
    for i in range(3):
      x = []
      for j in range(3):
        x.append("")
      vetor.append(x)
    return vetor

  def draw(self):
    """
    Imprime o tabuleiro.
    """
    print("   1  2  3")
    print("  -----------")
    for i in range(3):
      print("{} | {} | {}".format(self.tabuleiro[i][0], self.tabuleiro[i][1], self.tabuleiro[i][2]))
      print("  -----------")

  def verifica_vencedor(self):
    """
    Verifica se houve vencedor.

    Returns:
    O jogador vencedor, caso haja, ou `None`.
    """
    for linha in range(3):
      if self.tabuleiro[linha][0] == self.tabuleiro[linha][1] == self.tabuleiro[linha][2] != " ":
        return self.tabuleiro[linha][0]

    for coluna in range(3):
      if self.tabuleiro[0][coluna] == self.tabuleiro[1][coluna] == self.tabuleiro[2][coluna] != " ":
        return self.tabuleiro[0][coluna]

    if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != " ":
      return self.tabuleiro[0][0]
    elif self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != " ":
      return self.tabuleiro[0][2]

    return None

  def jogar(self, linha, coluna):
    """
    Faz uma jogada.

    Args:
      linha: A linha da jogada.
      coluna: A coluna da jogada.
    """
    if self.tabuleiro[linha][coluna] != " ":
      return False

    self.tabuleiro[linha][coluna] = self.jogadoratual
    self.jogadoratual = "X" if self.jogadoratual == "O" else "O"
    return True

  def fim_de_jogo(self):
    """
    Verifica se o jogo terminou.

    Returns:
    `True` se o jogo terminou, `False` caso contrário.
    """
    vencedor = self.verifica_vencedor()
    if vencedor is not None:
      return True

    for linha in range(3):
      for coluna in range(3):
        if self.tabuleiro[linha][coluna] == " ":
          return False

    return True

  def main(self):
    """
    Programa principal.
    """
    while True:
      self.draw()

      # Solicita a jogada do jogador atual
      self.jogada()

      # Verifica se o jogo terminou
      if self.fim_de_jogo():
        break

      vencedor = self.verifica_vencedor()
      if vencedor:
        print("O jogador {} venceu!".format(vencedor))
        break


if __name__ == "__main__":
  teste = JogoDaVelha()
  teste.main()
