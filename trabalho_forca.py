print("*** Jogo da forca ***\n")
print("*** Feito por cassio/lazaro/lorenzo!***\n")
palavraSecreta = input("Entre com a palavra secreta: ")
letrasDescobertas = []
percorrer = 0
contador = int(input("Entre com o número de chances: "))

for i in range(0,len(palavraSecreta)): #range = intervalo, len = até

    if palavraSecreta[i] == "-":
        letrasDescobertas.append("-") #append() = receba mesma quantidade que (-)
    else:
        letrasDescobertas.append("-")
print("".join(letrasDescobertas))

acertou = False #acertou = False - vai ficar repetindo até que acerte

while acertou is False:
    letra = input("Digite a letra de seu chute: ")  #emquanto "acertou = false" o programa vai pedir uma nova letra

    for i in range(0,len(palavraSecreta)):
        if letra == palavraSecreta[i]: #percorrer a palavra secreta para identificar se a letra que o usuario digitou esta na palavra secreta
            letrasDescobertas[i] = letra
            print("".join(letrasDescobertas))

    if letra not in palavraSecreta: # somar erros, caso erro = tentativas, encerrar.
        percorrer += 1
        print("Chances restantes:", contador - percorrer)
        if percorrer == contador:
            print("Você perdeu!")
            break

    if "-" not in letrasDescobertas: #se acabar os campos a serem preenchidos = ganhou
        print("Você ganhou com %d erros!" % percorrer)
        acertou = True