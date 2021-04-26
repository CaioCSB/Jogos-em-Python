import random
def jogar():
    print("*********************")
    print("****Jogo de forca****")
    print("*********************")

    #implementar o uso da lista de carros
    #carros = ["marea", "uno"]

    #uso da lista na busca de frutas
    frutas = ["maçã", "abacaxi", "uva", "laranja", "abacate", "tangerina", "figo", "acerola", "banana","romã", "manga", "mamão"]
    palavraSecreta = random.choice(frutas).upper()

    #para cada letra um _ no decorrer da palavra
    letrasAcertadas = ["_" for letra in palavraSecreta]

    #variaveis que param a aplicação se chegarem em true
    enforcado = False
    acertou = False
    tentativas = 0

    print("Você só possui 3 tentativas: ")

    print(letrasAcertadas)

    #o laço onde o define se o player acertou ou perdeu
    while (not enforcado and not acertou):
        #entrada de dados do player
        chute = input("Qual letra você quer chutar? ")
        chute = chute.strip().upper()

        if(chute in palavraSecreta):
            index = 0
            for letra in palavraSecreta:
                if (chute == letra):
                    letrasAcertadas[index] = letra
                index += 1
        else:
            tentativas += 1

        enforcado = tentativas == 3
        acertou = "_" not in letrasAcertadas
        print(letrasAcertadas)
    if(acertou):
        print("VOCÊ GANHOU CORNO(A)")
    else:
        print("VOCÊ É MUITO RUIM SEU OTARIO(A)")
        #futuramente arrumar a frase para determinado tipo de categoria
        print("A fruta era: ", palavraSecreta)
    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar()
