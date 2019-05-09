# -*- coding: utf-8 -*-
"""
Calculadora
Funções da calculadora: Fazer contas: soma, divisão, multiplicação, subtração
"""
print ("---- CALCULADORA v2.0 ----")
print ("Desenvolvida por: Eduardo")
print ("A calculadora suporta soma, subtração, multiplicação, divisão e exponenciação")
sair = False
while sair == False:	
	num1 = input("Digite o primeiro numero: ")
	num1 = int(num1)
	operador = input ("Digite o operador( +, -, /, *, **: ")
	num2 = input ("Digite o segundo numero: ")
	num2 = int(num2)
	
	#soma
	if operador == "+":
		operacao = num1 + num2

	#subtracao
	if operador == "-":
		operacao = num1 - num2

	#multiplicacao
	if operador == "*":
		operacao = num1 * num2

	#divisao
	if operador == "/":
		operacao = num1 / num2

	#exponenciacao
	if operador == "**":
		operacao = num1 ** num2

	print ("resultado: ")
	print (operacao)

	teste = input('deseja sair? (n/s)')
	if teste == 's':
		print ("obrigado por utilizar nossa calculadora")
		sair = True
