print("*************************************************************")
print("******************** JOGO DA ADIVINHAÇÃO ********************")
print("*************************************************************")

secret_number = 42
number_guess = 1

victory = 0

while number_guess < 6 and victory == 0:
    guess = int(input("Chute um número: "))
    print("Tentativa: ", number_guess)
    print("Você chutou: ", guess)
    number_guess = number_guess + 1
    if guess == secret_number:
        print("Parabéns! Você acertou!")
        victory = 1
    else:
        if guess > secret_number:
            print("Você errou! Seu chute foi MAIOR do que o número secreto!")
            print("Tente novamente!")
        elif guess < secret_number:
            print("Você errou! Seu chute foi MENOR do que o número secreto!")
            print("Tente novamente!")

print("*************************************************************")
print("********************     FIM DE JOGO     ********************")
print("*************************************************************")
