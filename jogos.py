import adivinhacao
import forca


def games():
    print("Qual jogo gostaria de jogar?\n(1) Adivinhação (2) Forca")
    game = int(input("Escolha: "))

    if game == 1:
        print("Você escolheu ADIVINHAÇÃO!\nDivirta-se!")
        adivinhacao.play()
    elif game == 2:
        print("Você escolheu FORCA!\nDivirta-se!")
        forca.play()


if __name__ == "__main__":
    games()
