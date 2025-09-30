import math
#===============================Exercício 1:==============================================================
#Faça um código capaz de calcular as raízes de uma equação de segundo grau no formato Ax2+Bx+C = 0.
#Considere as seguintes observações:
#• Se o termo A = 0 então a equação não é uma equação de segundo grau;
#• Seja ∆ = B2 − 4 × A × C. Se ∆ < 0 então a equação não possui raízes. Se ∆ = 0 então a equação
#possui apenas uma raiz.

def segundoGrau():

    print("informe os 3 valores:")
    a = float(input("valor 1: "))
    b = float(input("valor 2: "))
    c = float(input("valor 3: "))
    delta = 0

    if a == 0:
        print("Não é de segundo grau!")
    elif a != 0:
        delta = (b**2)-4*a*c 
        print (delta)

    if delta < 0:
        print("não possui raiz!")
    elif delta >= 0:
        resultado1 = ((-b+math.sqrt(delta))/(2*a))             # raiz quadrada (sqrt)
        print("resultado1:", resultado1)       
        resultado2 = ((-b-math.sqrt(delta))/(2*a))                 
        print("resultado2:", resultado2)    

#===============================Exercício 2:==============================================================
#Faça um código para determinar se um ano é ou não bissexto. Um ano N é bissexto se N é múltiplo de
#400, ou então se N é múltiplo de quatro, mas não é múltiplo de 100. Por exemplo, 2012 (múltiplo de 4,
#mas não múltiplo de 100) é bissexto, 1900 (múltiplo de quatro e de 100) não é bissexto, 2000 (múltiplo
#de 400) é bissexto).
def anoBissexto():
    valor = int(input("Informe um valor: "))
    if valor % 400 == 0: 
        print("é um ano bissexto")
    elif valor % 4 == 0 and valor %100 != 0:
        print("é um ano bissexto")
    else:
        print("não é um ano bissexto")

#===============================Exercício 3:==============================================================
#Considere a função range(início, fim, passo). Utilize essa função algumas vezes com variações nos
#parâmetros e faça laços de repetições para imprimir os valores gerados.
def aleatorio():
    for c in range(0, 100,2):
        print(c)
    for c in range(12, 1000,3):
        print(c)

#===============================Exercício 4:==============================================================
#Elabore um código que receba três notas considerando os pesos 0, 3, 0, 3 e 0, 4 para as notas 1, 2 e 3,
#respectivamente. A nota final é soma ponderada das três notas (NotaF inal = Nota1 ∗ 0, 3 + Nota2 ∗
#0, 3 + Nota4 ∗ 0, 3). O código deve receber estas notas para 10 alunos. É necessário informar se cada
#aluno foi aprovado (nota final maior ou igual a 60) ou não. Também deve ser informada a média final
#de todas as notas finais.

def mediaTurma():
    media = 0

    for c in range(10):
        n1 = float(input("Informe numero 1: "))
        n2 = float(input("Informe numero 2: "))
        n3 = float(input("Informe numero 3: "))

        resultado = (n1*0.3)+(n2*0.3)+(n3*0.4)
        media = media + resultado
        if resultado >= 60:
            print("aluno Aprovado")
        else:
            print("aluno reprovado")
    print("Media da turma: ", media/10)

#===============================Exercício 5:==============================================================
#Projete um código que leia uma quantidade indeterminada de números. A cada número informado, o
#usuário deve informar se deseja continuar ou parar. Ao final, o código deve retornar o maior e o menor
#número recebido.

numero = float (input ('Digite o valor do primeiro número: '))
numeroMaior = numero
numeroMenor= numero
while True: 
      continuar = input ('Deseja continuar(Sim/Não)?: ')
      if continuar == 'Sim' or continuar == 'sim':
       numero = float (input ('Digite o valor do proximo número: '))    
       if numero > numeroMaior:
                numeroMaior = numero
       if numero < numeroMenor:
                numeroMenor = numero    
      else:
        print ('Programa encerrado')    
        print (f"O valor do maior numero é {numeroMaior}, e o valor do menor numero é {numeroMenor}")
        break


#===============================Exercício 6:==============================================================
#Elabore um código que calcule o fatorial de um número recebido. O fatorial de um número n, representado
#por n!, é calculado da seguinte maneira n! = n × (n − 1) × ... × 2 × 1. Sendo que 1! = 0! = 1.
def fatorial():
    numero = int(input("Escreva um numero: "))
    resultado = numero
    numero = numero-1
    while numero !=0:
        resultado = resultado * numero 
        numero = numero -1
        if numero == 1:
            break
    print(resultado)

#==============================Exercício 7=============================================================
#Implemente o algoritmo de Euclides1 para calcular o máximo divisor comum (MDC) de dois números.
def mmc():
    a = int(input("Primeiro número: "))
    b = int(input("Segundo número: "))

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    print("MDC =", a)
#==============================Exercício 8=============================================================
#Crie um código que calcule o mínimo múltiplo comum (MMC) entre dois números. O MMC de dois
#números n1 e n2 pode ser calculado como MMC =
#n1∗n2 MDC , onde MDC é o máximo divisor comum entre n1 e n2.

numero1 = int (input ('Insira o valor do primeiro número(dividendo): '))
numero2 = int (input ('Insira o valor do segundo número(divisor): '))
mult = numero1*numero2
while numero2 != 0:
    resultado = numero1 % numero2
    numero1 = numero2
    numero2 = resultado
mdc=numero1
mmc = mult / mdc
print (f"O valor do MDC é {mdc}")
print (f"O valor do MMC é {mmc}")
#==============================Exercício 9=============================================================

#Elabore um código capaz de simular uma calculadora simples. O código deve solicitar ao usuário a
#operação desejada (soma, multiplicação, divisão, subtração ou potência) ou então sair. Quando o usuário
#escolhe uma operação, o programa deve solicitar dois números, realizar a operação sobre estes números
#e exibir o resultado. O código deve sempre solicitar uma nova operação até que o usuário escolha sair.
def calculadora():
    while True:
        print("====menu=== ")
        print("1 soma ")
        print("2 multiplicação")
        print("3 divisão")
        print("4 subtração")
        print("5 potencia")
        print("6 sair")
        escolha = int(input("Escolha: "))
        
        if escolha == 1:
            print("==Calculo== ")
            n1 = float(input("valor1: "))
            n2 = float(input("valor2: "))
            print (n1+n2)
        elif escolha == 2:
            n1 = float(input("valor1: "))
            n2 = float(input("valor2: "))
            print(n1*n2)
        elif escolha == 3:
            n1 = float(input("valor1: "))
            n2 = float(input("valor2: "))
            print(n1/n2)
        elif escolha == 4:
            n1 = float(input("valor1: "))
            n2 = float(input("valor2: "))
            print(n1-n2)
        elif escolha == 5:
            n1 = float(input("valor1: "))
            n2 = float(input("valor2: "))
            print(n1**n2)
        elif escolha == 6:
            break
#==============================Exercício 10=============================================================
#Desenvolva um código que, considerando um conjunto de números naturais A = {1, 2, 3, ..., n}, gere
#todas as combinações com três elementos contidos em A. Antes de gerar as combinações o programa
#deve perguntar o número de elementos de A ao usuário.

quantA = int (input ('Insira quantos valores você deseja inserir para A: '))

lista = list (range(1,quantA+1))
print (f"Conjunto A = {lista}")

for i in range(quantA):
    for j in range(quantA):
        for k in range(quantA):
            print((lista[i], lista[j], lista[k]))

#==============================Exercício 11=============================================================
#Considerando um conjunto A = {1, 2, 3, ..., n} com n informado pelo usuário, crie um código para obter
#os subconjuntos de três elementos contidos em A. Lembre-se que um conjunto não possui elementos
#repetidos.

n = int(input("infomee um valor")) 
contador = 0

lista = list(range(0,n))
print(lista)

for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        for k in range(j+1, len(lista)):
           print(lista[i],lista[j],lista[k])
           contador = contador + 1
print(contador)

#==============================Exercício 12=============================================================
#A função shuffle() da biblioteca random permite embaralhar uma lista de elementos. Utilizando essa
#função crie um código capaz de sortear elementos de uma lista. O usuário deve informar o número total
#de elementos e quantos elementos devem ser sorteados.

import random 

n = int (input ('Digite o numero total de elementos: '))
quantidade = int(input ('Digite quantos elementos devem ser sorteados: '))

lista = list(range(1,n+1))

random.shuffle(lista)

sorteados = lista [quantidade]

print (f"Lista completa {lista}")
print (f"Elementos sorteados {sorteados}")

#==============================Exercício 13=============================================================
#Projete um código que preencha uma lista de 100 posições com números de 1 a 10 (utilize a função
#randint() da biblioteca random). Em seguida, conte o número de vezes que cada número aparece e
#armazene em um segunda lista. Por fim, exiba a quantidade de veses que cada número apareceu.

import random

lista_numeros = [random.randint(1, 10) for _ in range(100)]

contagem = [0] * 10  

for numero in lista_numeros:
    contagem[numero - 1] += 1  

for i, qtd in enumerate(contagem):
    print(f"Número {i+1} apareceu {qtd} vezes")


#==============================Exercício 14=============================================================

while True:
    n = int(input('Digite o número de trechos da viagem (1 a 50): '))
    if 1 <= n <= 50:
        break
    print('Número inválido! Digite um valor entre 1 e 50.')

distancias = []
velocidades = []

for i in range(n):
    d = float(input(f'Digite a distância do trecho {i+1} (km): '))
    v = float(input(f'Digite a velocidade do trecho {i+1} (km/h): '))
    distancias.append(d)
    velocidades.append(v)


soma_distancia_velocidade = sum(distancias[i] * velocidades[i] for i in range(n))
soma_distancias = sum(distancias)
velocidade_media = soma_distancia_velocidade / soma_distancias

print(f"Velocidade média da viagem: {velocidade_media:.2f} km/h")
print('Trechos com velocidade acima da média:"')
for i in range(n):
    if velocidades[i] > velocidade_media:
        print(f"Trecho {i+1}: Velocidade = {velocidades[i]} km/h, Distância = {distancias[i]} km")
#==============================Exercício 15=============================================================
#Implemente um código capaz de ordenar os elementos de uma lista. Inicialmente, o código deve receber
#a quantidade de posições e um valor para cada posição. Em seguida, o código deve ordenar os elementos
#da lista utilizando o método bolha2
n = int(input("Digite a quantidade de elementos da lista: "))
lista = []
for i in range(n):
    valor = input(f"Digite o elemento {i+1}: ")
    lista.append(valor)

print(f"Lista inicial:, {lista}")

for i in range(n - 1):
    print(f"Passagem {i+1}:")
    trocou = False
   
    for j in range(n - 1 - i):
        if lista[j] > lista[j + 1]:
           
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
            trocou = True
            print(f"Troca {lista[j+1]} > {lista[j]}: {lista}")
        else:
            print(f"{lista[j]} ≯ {lista[j+1]} não troca: {lista}")
    else:
        break
print(f"Lista final ordenada:, {lista}")


#==============================Exercício 16=============================================================
#Desenvolva um código que receba uma lista de números inteiros e, sem seguida, crie uma nova lista
#contendo os mesmos números sem repetições.

entrada = input("Digite os números inteiros separados por espaço: ")
lista = [int(x) for x in entrada.split()]

lista_sem_repeticoes = []
for numero in lista:
    if numero not in lista_sem_repeticoes:
        lista_sem_repeticoes.append(numero)

print("Lista sem repetições:", lista_sem_repeticoes)

#==============================Exercício 17=============================================================

#Crie as funções input_int(mensagem) e input_float(mensagem) semelhantes à função input().
#As funções devem receber uma mensagem, exibi-la ao usuário e garantir que o número digitado seja
#válido. Enquanto o usuário digitar um número incorreto, as funções devem informar que o número é
#inválido e solicitar e digitação novamente. Faça uma chamada a cada função para testá-las. Dica: utilize
#a instrução try (tratamento de exceções).

def input_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Número inválido! Digite um inteiro válido.")

def input_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Número inválido! Digite um número decimal válido.")

idade = input_int("Digite sua idade: ")
print("Idade digitada:", idade)

altura = input_float("Digite sua altura em metros (ex: 1.75): ")
print("Altura digitada:", altura)

#==============================Exercício 18=============================================================
#Implemente o módulo mat.py contendo as seguintes funções:
#impar(numero): Retorna True ou False, caso o numero seja impar ou não;
#area_circulo(raio): retorna a área de um círculo a partir de seu raio, área = raio2 × π (dica, importe
#pi da biblioteca math)
#Codifique as chamadas a essas funções em outro arquivo.

import math
def impar(numero):
    return numero % 2 != 0
def area_circulo(raio):
    return math.pi * (raio ** 2)

import mat 
num = int(input("Digite um número inteiro: "))
if mat.impar(num):
    print(f"O número {num} é ímpar.")
else:
    print(f"O número {num} não é ímpar.")


raio = float(input("Digite o raio do círculo: "))
area = mat.area_circulo(raio)
print(f"A área do círculo de raio {raio} é {area:.2f}")

#==============================Exercício 19=============================================================
#Construa um programa que receba uma data do usuário (mês e ano) e mostre o resultado das funções
#implementadas sobre essa data.
def ano_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)


def dias_mes(ano, mes):
    if mes == 2:
        return 29 if ano_bissexto(ano) else 28
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return None 

def nome_mes(mes):
    nomes = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    if 1 <= mes <= 12:
        return nomes[mes - 1]
    else:
        return None  


import datas

ano = int(input("Digite o ano: "))
mes = int(input("Digite o mês (1 a 12): "))

if datas.ano_bissexto(ano):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")

dias = datas.dias_mes(ano, mes)
if dias is not None:
    print(f"O mês {mes} ({datas.nome_mes(mes)}) tem {dias} dias.")
else:
    print("Mês inválido!")

nome = datas.nome_mes(mes)
if nome:
    print(f"Nome do mês {mes}: {nome}")

#==============================Exercício 20=============================================================
#Escreva um módulo com funções para calcular o máximo divisor comum (MDC) e o mínimo múltiplo
#comum (MMC) de uma lista de números. Dica: comece calculando o MDC dos dois primeiros números e,
#depois, para cada número, calcule o MDC desse número com o resultado anterior (o MMC pode ser feito
#de fórmula análoga). Implemente também chamadas a essas funções números digitados pelo usuário.
def mdc_dois(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mdc_lista(numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado = mdc_dois(resultado, num)
    return resultado


def mmc_dois(a, b):
    return a * b // mdc_dois(a, b)

def mmc_lista(numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado = mmc_dois(resultado, num)
    return resultado


import matematica

entrada = input("Digite os números separados por espaço: ")
numeros = [int(x) for x in entrada.split()]


mdc = matematica.mdc_lista(numeros)
print(f"MDC dos números {numeros} = {mdc}")

mmc = matematica.mmc_lista(numeros)
print(f"MMC dos números {numeros} = {mmc}")