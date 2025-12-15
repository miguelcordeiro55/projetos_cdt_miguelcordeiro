import random

tabuleiro = [" " for _ in range(9)]

def mostrar_tabuleiro():
    print()
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---+---+---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---+---+---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print()

def vencedor(jogador):
    combinacoes = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    return any(tabuleiro[a] == tabuleiro[b] == tabuleiro[c] == jogador
               for a, b, c in combinacoes)

def jogada_bot():
    posicoes_livres = [i for i in range(9) if tabuleiro[i] == " "]
    return random.choice(posicoes_livres)

def jogo():
    jogador_atual = "X"

    for _ in range(9):
        mostrar_tabuleiro()

        if jogador_atual == "X":
            while True:
                try:
                    jogada = int(input("Escolha uma posição (1-9): ")) - 1
                    if jogada < 0 or jogada > 8:
                        print("Digite um número entre 1 e 9.")
                    elif tabuleiro[jogada] != " ":
                        print("Posição ocupada. Escolha outra.")
                    else:
                        break
                except ValueError:
                    print("Digite apenas números.")
        else:
            jogada = jogada_bot()
            print(f"Bot escolheu a posição {jogada + 1}")

        tabuleiro[jogada] = jogador_atual

        if vencedor(jogador_atual):
            mostrar_tabuleiro()
            print("🎉 Você venceu!" if jogador_atual == "X" else "😱 O bot venceu!")
            return

        jogador_atual = "O" if jogador_atual == "X" else "X"

    mostrar_tabuleiro()
    print("😐 Deu velha!")

jogo()
