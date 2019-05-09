# -*- coding: utf-8 -*-
"""
Jogo: Par ou Impar
Autor: Eduardo
"""
from random import randint
print ("--- Jogo PAR ou IMPAR v1.0 ---")
print ("Desenvolvido por: Eduardo")
sair = False
while sair == False:	
	num1 = input("Selecione um número de 0 a 10: ")
	num1 = int(num1)
	if num1 % 2 == 0:
		print("o seu número selecionado é: ")
		print ("par")
		j1 = "p"
	else:
		print("o seu número selecionado é: ")
		print ("impar")
		j1 = "i"
	num2 = randint (0,1)
	#print ("o computador selecionou: ")
	#print (num2)

	if num2 % 2 == 0:
		print("o computador jogou um número par ")
	#	print ("par")
		j2 = "p"
	else:
		print("o computador jogou um número impar")
	#	print ("impar")
		j2 = "i"

	if j1 == "p" and j2 == "p":
		print ("Você ganhou!")
	elif j1 == "p" and j2 == "i":
		print ("Você perdeu!")
	elif j1 == "i" and j2 == "p":
		print ("Você ganhou!")
	else:
		print ("Você perdeu!")

	teste = input('deseja sair? (n/s)')
	if teste == 's':
		print ("obrigado por utilizar nosso programa")
		sair = True

