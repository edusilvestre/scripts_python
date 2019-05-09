# -*- coding: utf-8 -*-
"""
Script feito para verificar se a divisão é perfeita ou sobra resto
Autor: Eduardo
"""
print ("--- Verifica divisão v1.0 ---")
print ("Desenvolvido por: Eduardo")
print ("Script feito para verificar se a divisão é perfeita ou sobra resto")
sair = False
while sair == False:
	num1 = input("Insira o número que será dividido: ")
	print ("o dividendo é: ")
	print (num1)
	num1 = int(num1)
	num2 = input("Insira o número que você deseja dividir o número acima: ")
	print ("o divisor é: ")
	print (num2)
	num2 = int(num2)
	operacao = num1 / num2
	verificador = num1 % num2
	print ("o resultado da divisão é: ")
	print (operacao)

	if verificador == 0:
		print ("divisao perfeita")
	else:
		print ("divisao com resto, imperfeita")
		print('o resto é: ')
		print(verificador)

	teste = input('deseja sair? (n/s)')
	if teste == 's':
		print ("obrigado por utilizar nosso programa")
		sair = True