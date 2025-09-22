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