'''


		LIBS


'''
from math import *
import math
from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot
from numpy.polynomial import Polynomial as P
from numpy import polynomial



def f(fx,x):#definindo a função matematica
   f = eval(fx)
   return f


def newton():

    pontos = []
    k = 0
    while True:
        k += 1
        while True:
            print("Digite as coordenadas do ", k, "º ponto separados por espaço:", end="\nf para finalizar \n")
            l = input()  # irá receber a entrada do usuário
            if l == "f".lower():  # Verifica se o usuário quer terminar a entrada de dados
                break
            l = l.split()  # transforma a entrada do usuário numa lista de strings
            if len(l) == 2:  # verifica se o usuário entrou com um ponto do R2
                break
            else:
                print("Entrada inválida, tente novamente!")
        if l == "f".lower():
            break
        for i in range(len(l)):  # transfoma a entrada do usuário em um ponto e adiciona a lista de pontos
            l[i] = float(l[i])
        pontos.append(l)

    l = []
    for i in range(len(pontos)):
        l.append(pontos[i][1])
    tabela = []  # Será a tabela de diferenças divididas
    tabela.append(l)
    # Calcula as diferenças divididas
    # o polinômio a+bX+cX^2 eu tenho que escrever P([a,b,c]), logo P([1,2,3...n]) = 1+2x+3x^2+....nx^(n-1)
    for i in range(len(pontos) - 1):
        l = []  # lista que irá receber as diferenças divididas de ordem i+1
        for j in range(len(pontos) - i - 1):
            # calculando a j+1 difença dividida de ordem i+1
            dif = (tabela[i][j + 1] - tabela[i][j]) / (pontos[j + 1 + i][0] - pontos[j][0])
            l.append(dif)
        tabela.append(l)  # adiciona a tabela de diferenças divididas as difenças divididas de ordem i+1
    difdiv = []  # irei pegar a primeira diferença dividida de cada ordem e adicionar a essa lista,
    # pois elas corresponderão a d0, d1... dn do polinômio como na fórmula da página 220 do livro
    for i in range(len(tabela)):
        difdiv.append(tabela[i][0])
    # Aqui será feito o Somatório do final da página
    somatorio = 0
    for i in range(1, len(pontos)):
        produtorio = 1
        for k in range(i):  # Aqui será feito o produtório do final da página
            produtorio *= (P([-pontos[k][0], 1]))  # P([-pontos[k][0], 1]) = (X-Xk)
        somatorio += difdiv[i] * produtorio
    Pn = difdiv[0] + somatorio
    funcao = list(Pn)  # tranformo o polinômio em lista
    # transformando o polinômio para uma formato mais legível
    texto = ""
    for i in range(len(funcao)):
        if funcao[i] == 0:
            continue
        elif i == 0:
            texto += str(funcao[i])
        else:
            texto += " + " + str(funcao[i])
            texto += ("*x^%o" % (i))
    print("Pn(x) :")
    print(texto)
    s = input(
        "Deseja calcular Pn(x) dado um valor de x? \n [S/N]").lower()  # para desativar essa função é só colocar ""# depois de s=
    if s == "s":
        print("Pn(x) em qual ponto?")
        p = float(input())
        print("Pn(%a) é igual a %a" % (p, Pn(p)))
    print("Raízes de Pn(x): ", polynomial.polynomial.polyroots(list(Pn)))
    s = input(
        "Encontrar os valores de x dado um valor de Pn(x)? \n [S/N]")  # para desativar essa função é só colocar ""# depois de s=
    if s == "s":
        print("Valores de x para qual valor de Pn(x)")
        p = float(input())
        print("para Pn(x)=%a temos: " % p, polynomial.polynomial.polyroots(list(Pn - P([p]))),
              "Obs: Se houver, j = raiz de menos 1")
    # calculando f(x) nos pontos dados através de Pn(x)
    print("(x,Pn(x))")
    for i in range(len(pontos)):
        print("(%a,%a)" % (pontos[i][0], round(Pn(pontos[i][0]), 4)))
    
'''


		METODO DE SIMPSON


'''

def simpson():
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





'''


		METODO DE JACOBI


'''

def jacobi(A, b, N=2000):

    x = zeros(len(A[0]))
    x_ant = zeros(len(A[0]))
    D = diag(A)
    R = A - diagflat(D)

    for i in range(N):
        x = (b - dot(R, x)) / D
        if(x.all() == x_ant.all()):
            return x
        x_ant = x
    return x


def _print_arrays(number_of_variables):
    print("\n\n\n Your table:\n\n")
    for collumn in range(0, number_of_variables):
        print("|-----", end='')
    print("|   |----|   |----|")

    for row in range(0, number_of_variables):
        for collumn in range(0, number_of_variables):
            print("| A"+str(row)+str(collumn), end=' ')
        if(row == number_of_variables//2):
            print("| . | X"+str(row)+" | = | b"+str(row)+" |")
        else:
            print("|   | X"+str(row)+" |   | b"+str(row)+" |")

    for collumn in range(0, number_of_variables):
        print("|-----", end='')
    print("|   |----|   |----|\n\n\n")


def _print_arrays_final(number_of_variables, A, b, x):
    print("\n\n\n Your table:\n\n")
    for collumn in range(0, number_of_variables):
        print("|------", end='')
    print("|   |-------|   |------|")

    for row in range(0, number_of_variables):
        for collumn in range(0, number_of_variables):
            print("| "+"{0:.2f}".format(A[row][collumn]), end=' ')
        if(row == number_of_variables//2):
            print("| . | "+"{0:.2f}".format(x[row]) +
                  " | = | "+"{0:.2f}".format(b[row])+" |")
        else:
            print("|   | "+"{0:.2f}".format(x[row]) +
                  " |   | "+"{0:.2f}".format(b[row])+" |")

    for collumn in range(0, number_of_variables):
        print("|------", end='')
    print("|   |------|   |------|\n\n\n")


def _get_A_array(number_of_variables):
    temp_collumn = []
    A = []
    for row in range(0, number_of_variables):
        for collumn in range(0, number_of_variables):
            temp_collumn.append(
                float(input("Type the A"+str(row)+str(collumn)+" :")))
        print("")
        A.append(temp_collumn)
        temp_collumn = []
    return array(A)


def _get_b_array(number_of_variables):
    b = []
    for variable in range(0, number_of_variables):
        b.append(
            float(input("Type the b" + str(variable) + " :")))
    print("")
    return array(b)

# Start of the program

def jacobi1():
    number_of_variables = int(input("How many variables do you want to have? "))
    _print_arrays(number_of_variables)
    A = _get_A_array(number_of_variables)

    b = _get_b_array(number_of_variables)

    x = jacobi(A, b)

    _print_arrays_final(number_of_variables, A, b, x)


'''


		METODO DA BISSECÇÃO


'''

def trun_n_d(n,d):
    s=repr(n).split('.')#dando split no numero pelo "." criando uma lista com 2 valores , um com o numero inteiro e outro com um numero decimal
    if (len(s)==1):
        return int(s[0])#se s só tiver 1 valor é porque o numero ja é inteiro , por isso retorna ele mesmo
    return float(s[0]+'.'+s[1][:int(d)])#retorna o numero inteira + "." + o 1 valor + uma sequencia de numeros definida por "d"
def bisseccao():
   fx = input("Insira a função: ")

   a = float(input("Insira a: "))#1º Valor do intervalo [a,b]
   b = float(input("Insira b: "))
   p = float(input("Insira a precisão(Entre 1 - 16): "))#Numero de casas decimais
   pl = 10**(-p)#Definindo a precisão em numeros decimais 
   if (f(fx ,a)*f(fx ,b) < 0):#Aplicando Bozzano
      x = (a+b)/2#1ª media do intervalo
      
      if (f(fx,x)*f(fx,b)<0):#Define se o Numero achado será o novo "a" ou o novo "b"
         a = x
      else:
         b = x
      while (abs(f(fx,x))>pl):#Cria um loop em que ele só termina caso o numero atender a precisão
         x = (a+b)/2
         if (f(fx,x)*f(fx,b)<0):
            a = x
         else:
            b = x
      x = trun_n_d(x,p)#Trunca o  numero pra caber na precisão
      print("A raiz da função , com precisão de {} casas decimais , é {}".format(p,x))
   else:
      print("Não tem raiz unica no intervalo")#Caso Bozzano esteja falso
'''


		DEFININDO A GRAPHIC INTERFACE


'''
gui1 = """
======================================
|Digite (1) para -> Zeros da Função  
|Digite (2) para -> Interpolação	 
|Digite (3) para -> Integração		 
|Digite (4) para -> Sistemas Lineares
|Digite (0) para -> SAIR			 
======================================
"""
gui2 = """
===============================
|Digite (1) para -> Bissecção 
|Digite (2) para -> Newton	  
===============================
"""
gui3 = """
===============================
|Digite (1) para -> Newton    
|Digite (2) para -> Lagrange  
===============================
"""
gui4 = """
===============================
|Digite (1) para -> Simpson 
|Digite (2) para -> Trapézios  
===============================
"""
gui5 = """
===============================
|Digite (1) para -> Jacobi    
|Digite (2) para -> LU   	  
===============================
"""
guin = """
===============================
|Opção inválida no momento    |
===============================
"""
guiout = """
===============================
|Obrigado e adeus!            |
===============================
"""
'''


		RODANDO O FLUXO DE TELAS


'''
while True:
	x = int(input(gui1))

	if x == 1:
		y = int(input(gui2))
		if y == 1:
			bisseccao()
			continue
		else:
			print(guin)
			continue
	elif x == 2:
		y = int(input(gui3))
		if y == 1:
			newton()
			continue
		else:
			print(guin)
	elif x == 3:
		y = int(input(gui4))
		if y == 1:
			simpson()
			continue
		else:
			print(guin)
			continue
	elif x == 4:
		y = int(input(gui5))
		if y == 1:
			jacobi1()
			continue
		else:
			print(guin)
			continue
	elif x == 0:
		print(guiout)
		break
