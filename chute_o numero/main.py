import random


def sortear_numero():
    return random.randint(1, 100)


def verifica_resposta(resposta):
    resposta = resposta.strip().lower().replace("ã", "a")
    while resposta != "sim" and resposta != "nao":
        resposta = str(input("Por favor, difite uma resposta valida? Sim ou Não?"))
        resposta = resposta.strip().lower().replace("ã", "a")

    if resposta == "sim":
        return True
    elif resposta == "nao":
        return False


def pede_numero():
    while True:
        try:
            nro = int(input("\nTente a acretar o numero. "))
            break
        except ValueError:
            print("Por favor, informe um numero inteiro ")

    return nro


def jogar():
    print("Adivinhacao (Chute o numero)")
    print("____________________________\n\n")

    resposta = str(input("Quer jogar o jogo da adivinhacao? Sim ou Não?"))
    quer_jogar = verifica_resposta(resposta)

    if quer_jogar:
        nro_sorteado = sortear_numero()
        while quer_jogar:
            nro_escolhido = pede_numero()
            if nro_sorteado > nro_escolhido:
                print("O numero secreto é maior que " + str(nro_escolhido) + "!")
            elif nro_sorteado < nro_escolhido:
                print("O numero secreto é menor que " + str(nro_escolhido) + "!")
            elif nro_escolhido == nro_sorteado:
                resposta = str(input("Parabens, Voce Acertou! \n\nGostaria de jogar novamente? Sim ou Não?"))
                if verifica_resposta(resposta):
                    nro_sorteado = sortear_numero()
                    continue
                else:
                    print("\nAte a Proxima!")
                    break
            else:
                print("Tente outra vez!")
    else:
        print("\nAte a proxima!")


jogar()

