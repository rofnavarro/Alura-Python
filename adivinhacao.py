print("*************************************************************")
print("******************** JOGO DA ADIVINHAÇÃO ********************")
print("*************************************************************")

secret_number = 42

guess = int(input("Chute um número: "))
print("Você chutou: ", guess)

correct = secret_number == guess
bigger = secret_number < guess
smaller = secret_number > guess

if(correct):
    print("Parabéns! Você acertou!")
else:
    if(bigger):
        print("Você errou! Seu chute foi MAIOR do que o número secreto!")
    elif(smaller):
        print("Você errou! Seu chute foi MENOR do que o número secreto!")

print("*************************************************************")
print("********************     FIM DE JOGO     ********************")
print("*************************************************************")
