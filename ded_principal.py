import os
os.system("cls")
#Jogar 4 D6 e diminuir o menor dado a soma dos dados
import random
Dado1=random.randrange(1,6)
Dado2=random.randrange(1,6)
Dado3=random.randrange(1,6)
Dado4=random.randrange(1,6)

soma_dados=(Dado4+Dado1+Dado2+Dado3)

dados=[Dado1,Dado2,Dado3,Dado4]
menor_dado=min(dados)
atributos=(Dado1+Dado2+Dado3+Dado4-menor_dado)

print("Os dados são: ", Dado1,Dado2,Dado3,Dado4)
print("Soma dos dados são: ",soma_dados)
print("O menor dado foi: ",menor_dado)
print("Seu atributo foi de: ",atributos)
