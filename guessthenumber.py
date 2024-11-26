print("indovina il numero casuale da 1 a 100 per vincere il gioco")
i = 0
while i == 0:
    import random
    guess = int(input("inserisci il numero: "))
    numero1 = random.randint(0, 10)
    if guess == numero1:
        print("hai vinto!")
        i += 1
    else:
        print("riprova")
