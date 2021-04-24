def jogar():
    print("*********************")
    print("****Jogo de forca****")
    print("*********************")

    palavraSecreta = "abacaxi"
    letrasAcertadas = ["_", "_", "_", "_", "_", "_", "_"]

    enforcado = False
    acertou = False
    tentativas = 0

    print(letrasAcertadas)

    while (not enforcado & acertou):

        chute = input("Qual letra você quer chutar? ")
        chute = chute.strip()

        index = 0
        if(chute == palavraSecreta):
            index = 0
            for letra in palavraSecreta:
                if (chute.upper() == letra.upper()):
                    letrasAcertadas[index] = letra
                index = index + 1
        else:
            tentativas = tentativas + 1

        enforcado = tentativas == 2
        print(letrasAcertadas)


if(__name__ == "__main__"):
    jogar()
