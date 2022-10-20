def play():
    print("*************************************************************")
    print("********************    JOGO DA FORCA    ********************")
    print("*************************************************************")

    secret_word = "cachorro"

    correct = False
    win = False

    letra = input("Escolha uma letra: ")

    while not correct and not win:
        print("Jogando...")

    print("*************************************************************")
    print("********************     FIM DE JOGO     ********************")
    print("*************************************************************")


if __name__ == "__main__":
    play()
