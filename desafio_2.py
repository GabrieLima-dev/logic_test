def partida():
    lista = [0, 1, 2, 3, 4]
    x = ""
    y = ""
    while x not in lista:
        x = int(input(
            "Digite o número de gols do Time 1 nesta partida.\n OBS: Apenas digite números de 0 a 4   "))

    while y not in lista:
        y = int(input(
            "Digite o número de gols do Time 2 nesta partida.\n OBS: Apenas digite números de 0 a 4   "))

    print("O resultado desta partida foi {}:{}".format(x, y))


def n_partida():
    numeroPartida = 1
    while numeroPartida <= 10:
        print()
        print('**** Partida', numeroPartida, '****')
        print()
        partida()
        numeroPartida += 1


print("Olá, nosso jogo irá começar.\n Teremos 10 partidas.\n Que vença o melhor time!")
print()
n_partida()
