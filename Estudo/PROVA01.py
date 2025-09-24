#------------- PROVA MARCOS 23-09---------------------
numero = 11
numero1 = 23.09
print(numero,numero1)


# ENTRADA DE DADOS (os valores são em formato de string)

valor = input ("Informe um valor: ")
print(valor)
valor2 = int(input("Informe um numero inteiro: ")) # converter o valor para Inteiro
print ("Valor escolhido: ", valor2)
valor3 = int(input ("informe um valor: "))

print (valor3**2)  # potencia (elevado a...)
print ("valor //: ", valor3//valor2) # divisão inteira (int)
print ("valor /: ", valor3/valor2)  # divisão fracvionada (float)
#--------- Operadores logicos --------------

v1 = 5
v2 = 10

v3 = (v1> v2)
print(v3)
v3 = (v1< v2)
print(v3)
v3 = (v1== v2)
print(v3)
v3 = (v1!= v2)
print(v3)
#--------- condicional (IF)--------------

if(1>10):
    print ("aprovado")     #(OBS) 4 espaços para ser dentro de um bloco (    )
else:
    if(1!=1):
        print("reprovado")
    else:
        print("Não")
print ("fora do IF")
#-- ELIF -- (else if)
#  elif (N>1):

# ------- CALCULADORA --------------

print("=== calculadora ===")
n1 = int(input("Valor 1: "))
n2 = int(input("valor 2: "))
calculo = input("Operação: +,-,/,*:" )

if(calculo == "+"):
    print(n1+n2)
elif(calculo == "-"):
    print(n1-n2)
elif(calculo =="/"):
    print(n1/n2)
else:
    print(n1*n2)

#--------   ESTRUTURA DE REPETIÇÃO (for/ while) ---------------------
#  while

n= 10
i = 0

while i<10:
    print(i)
    i = i+1

# for

for c in range (10):
    print(c)
while True:
    n = input ("Infome um numero: ")
    if n == "0":
        break
    else:
        print("Numero: ",n)
# continue: “pula” para a próxima iteração da repetição,

#---------------- listas--------------------------- 55

lista_precos = []

lista_precos.insert(0,12)
lista_precos.insert(1,13)
print(lista_precos[1])

#---------------- funções --------------------------- 55

def NomeDaFuncao():
    return v1  # se a função retornar alguma coisa


#------------------Recursão------------------------


#------------- arredondamento --------------------
print(round(1.34))