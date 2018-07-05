x = []
fx = []
i = 0
I = 0
P = 0

#inputs dos pontos do intervalo e o número de partes em que é dividido
a = float(input('Valor de A: '))
b = float(input('Valor de B: '))
n = int(input('Partes divididas: '))

#formula ponto medio
h = (b - a) / (n)

while i < n:
    #input para os pontos da função
    num_x = float(input('Digite x{0}: '.format(i)))
    num_fx = float(input('Digite fx{0}'.format(i)))
    x.append(num_x)
    fx.append(num_fx)

    #se o valor de i for diferente de zero, seja par e diferente do numero de partes
    #em que o intervalo é dividido a função do pol é utilizada
    if (i != 0) and ((i % 2) == 0) and (i != (n)):
        P += x[i] * fx[i]

    # //               , seja impar e diferente do numero de partes
    #em que o intervalo é dividido, a função de integração é utilizada
    elif (i != 0) and ((i % 2) != 0) and (i != (n)):
        I += x[i] * fx[i]

    i += 1

E = (x[0] * fx[0]) + (x[n-1] * fx[n-1])

#formula simpson
Simpson = (h / 3) * (E + (4 * I) + (2 * P))

print('O valor da integral é: {0:.3f}'.format(Simpson))
