import os
os.system("cls")

import random 
atributos=1

while atributos:
    Dado_1=random.randint(1,6)
    Dado_2=random.randint(1,6)
    Dado_3=random.randint(1,6)
    Dado_4=random.randint(1,6)

dados=[Dado_1,Dado_2,Dado_3,Dado_4]
menor_dado=min(dados)

soma_dados=(Dado_1+Dado_2+Dado_3+Dado_4)

print("Número aleatório gerado: ",Dado_1,Dado_2,Dado_3,Dado_4)
print("A soma dos seus números foi: ",soma_dados)
print("O resultado foi: ",soma_dados-menor_dado)
    
continuar=int(input("Gerar novamente?\n1.sim\n0.Não\n"))
