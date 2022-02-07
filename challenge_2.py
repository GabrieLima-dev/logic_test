temp = []
princ = []


def match():
    list = [0, 1, 2, 3, 4]
    x = ""
    y = ""
    while x not in list:
        x = int(input(
            "Digite o número de gols do Time 1 nesta partida.\n OBS: Apenas digite números de 0 a 4   "))

    while y not in list:
        y = int(input(
            "Digite o número de gols do Time 2 nesta partida.\n OBS: Apenas digite números de 0 a 4   "))

    print()
    print("O resultado desta partida foi {}:{}".format(x, y))
    pointing(x, y)


def pointing(a, b):
    if a > b:
        temp.append(3)
    if a < b:
        temp.append(0)
    if a == b:
        temp.append(1)
    princ.append(temp[:])


def n_match():
    numberMatch = 1
    while numberMatch <= 10:
        print()
        print('**** Partida', numberMatch, '****')
        print()
        match()
        numberMatch += 1


print("Olá, nosso jogo irá começar.\n Teremos 10 partidas.\n Que vença o melhor time!")
print()
n_match()
print()
print("-" * 60)
print("O nosso time ao fim do campeonato teve um total de {} pontos.".format(
    sum(princ[9])))
print("-" * 60)
