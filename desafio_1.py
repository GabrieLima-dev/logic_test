from ast import Break


date = int(input("Informe aqui uma data e lhe direi em qual século está: "))

D = date
d = 100
q = int(date/d)
r = date % d
x = q + 1

if D < 100:
    print("Com o ano {} estamos falando do século 1".format(D))

if D > 100:
    D = q * d + r
    if r == 0:
        print("Com o ano {} estamos falando do século {}".format(D, q))
    else:
        print("Com o ano {} estamos falando do século {}".format(D, x))
