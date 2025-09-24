
import numpy as np

#============= NumPay =====================

# é usada para trabalhar com arrais (Vetores)



# Criando arrays
a = np.array([1, 2, 3, 4])
b = np.arange(0, 10, 2)
c = np.random.randint(0, 10, (3, 3))
print('Array a:', a)
print('Array b:', b)
print('Matriz c:\n', c)

# Operações matemáticas
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print('Soma:', x + y)
print('Multiplicação:', x * y)
print('Média:', np.mean(x))


# Indexação e fatiamento
matriz = np.arange(1, 10).reshape(3, 3)
print('Matriz:\n', matriz)
print('Primeira linha:', matriz[0])
print('Coluna do meio:', matriz[:,1])

# a) v= raiz 2x981*20 = 198,1 cm/s
# b) 198,1*2,5
# C) ten = 1560cm^2/ 495,25cm    = 3,14s
# O canal de alimentaçã oque leva o metal ate o canal de ataque de um molde tem 175mm de comprimento. a area da sesão transversal é 400mm^2. 
# A cavidade do modulo tem volume igual a 0,001m^3. 
# a)Determine a velocidade do mental fundido na base do canal de alimentação 
# b) Vasão do fluxo
#c) tempo nessesario papa preencher (tempo de enchimento do molde)
#
#
#
#
