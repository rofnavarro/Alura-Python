import random

print("*************************************************************")
print("******************** JOGO DA ADIVINHAÇÃO ********************")
print("*************************************************************")

secret_number = round(random.randrange(1, 101))
total_guess = 0
score = 1000

print("Qual o nível de dificuldade?\n(1) Fácil (2) Médio (3) Difícil")
level = int(input("Nível: "))

if level == 1:
    total_guess = 20
elif level == 2:
    total_guess = 10
elif level == 3:
    total_guess = 5

for number_guess in range(1, total_guess + 1):
    print("Tentativa: {} de {}".format(number_guess, total_guess))

    guess = int(input("Chute um número entre 1 e 100: "))
    print("Você chutou: ", guess)

    if guess < 1 or guess > 100:
        print("O número deve ser entre 1 e 100!")
        continue

    if guess == secret_number:
        print("Parabéns!\nVocê acertou e fez {} pontos!".format(score))
        break
    else:
        lost_points = abs(secret_number - guess)
        score = score - lost_points

        if guess > secret_number:
            print("Você errou!\nSeu chute foi MAIOR do que o número secreto!")
            if number_guess == total_guess:
                print("O número secreto era {}. Você fez {} pontos".format(secret_number, score))
        elif guess < secret_number:
            print("Você errou!\nSeu chute foi MENOR do que o número secreto!")
            if number_guess == total_guess:
                print("O número secreto era {}. Você fez {} pontos".format(secret_number, score))

print("*************************************************************")
print("********************     FIM DE JOGO     ********************")
print("*************************************************************")
