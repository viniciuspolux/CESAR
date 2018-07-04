# Método de Integração de Simpson
# Função de integração: x * f(x) 
# Mudar função dentro do código

while True:

    x = []
    fx = []
    i = 0
    I = 0
    P = 0
    n = int(input('Número de pontos: '))

    if (n % 2) != 0:

        a = float(input('Valor inicial: ')) 
        b = float(input('Valor final: '))
        h = (b - a)/n

        while i < n:
            num_x = float(input(' x{0}: '.format(i)))
            num_fx = float(input(' fx{0}: '.format(i)))
            x.append(num_x)
            fx.append(num_fx)

            if (i != 0) and ((i % 2) == 0) and (i != (n - 1)):
                P += x[i] * fx[i]
            elif (i != 0) and ((i % 2) != 0) and (i != (n - 1)):
                I += x[i] * fx[i]

            i += 1

        E = (x[0] * fx[0]) + (x[n-1] * fx[n-1])

        Simpson = (h / 3) * (E + (4 * I) + (2 * P))  

        print('O valor da integral é: {0:.3f}'.format(Simpson))
        
        break
        
    else:
        
        print('O número de pontos precisa ser ímpar.')  