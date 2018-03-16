#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Criado por Rafael F S Requiao @ Python 3.6.4 (brew) - macOS 10.11

#----------------------------------------

# IMPORTS

from __future__ import division, print_function, unicode_literals
import os, sys, string, time, codecs, re, click


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# implementar Wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# implementar interacao do teclado e mouse
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions

from selenium.common.exceptions import TimeoutException
timeout = 20
esperar = 10

#implementar tex2pdf

import tex, texcaller, io
from io import StringIO, BytesIO



#----------------------------------------

# VARIÁVEIS GLOBAIS

global resolucao_steps
global expressao
expressao = ""

global math_type
math_type = ""

#global input_formats = ['asciimath', 'latex', 'mathml']

global output_formats
output_formats = ['tex', 'mathml']

global bode
bode = ""

global calculos_element
calculos_element = ""

global firefox
firefox = ""

#----------------------------------------

# FUNÇÕES


def LimparTela():
	os.system('cls' if os.name=='nt' else 'clear')

#fim de LimparTela()


def DesceJanelaUmPouco(num):
	global bode
	
	# Tirar bug caso o mouse clique em algum lugar fora da visualizacao
	# Parece que descer teclas buga tudo - foda-se
	print("[DEBUG] Descer a tela...")
	for i in range(0, num) :
		bode.send_keys(u'\ue015')

#fim de DesceJanelaUmPouco()


def Resolucao(math_type):
	global resolucao_steps
	global calculos_element
	global firefox
	
	
	print("[DEBUG] obter todos os div.calc-math e meter numa lista")

	print("[DEBUG] math_type = " + math_type)


	if math_type == "tex":
	
		try:
			calculos_element = 	firefox.find_elements_by_class_name(
									"calc-math"
								)

		#calculos_element = 	firefox.find_elements_by_xpath(
		#						#"//div[@class='calc-math']"  #TeX
		#						"//span[@id='MathJax*']"
		#					)
										
		# Tratar elemento do Firefox antes de imprimir
					
		except:
			print("[DEBUG] erro... sem calc-math... :( ")


	if math_type == "mathml":
	
		try:
			# DEBUG MathML
			# limitar melhor o que aparece dentro daquele div.calc-math
			# to pegando coisas de fora
			calculos_element = 	firefox.find_elements_by_class_name("mjx-chtml")
	
		except:
			print("[DEBUG] erro... sem mjx-chtml... :( ")




	#pegar TeX de cada calc-math - element <script> ; type="math/tex"
	indice=0
	resolucao_steps=[] #talvez mudar isso aqui pra outro lugar
	
	for calculo in calculos_element:
		
		if math_type == "tex" :
		
				#DEBUG TeX
			
				temp = codecs.encode(calculo.text , 'utf-8')
				#atributo1 = calculo.get_attribute("id")
				#atributo2 = calculo.get_attribute("type")
				#print("indice = " + str(indice) + " " + str(atributo1) + " " + str(atributo2) + " --> " + str(temp))
		
				#WIP TeX - método #01
				#pré-processar calculo.text
				#só existe o método .text na classe WebElement...?
				#posso usar algum get (innerHTML/outerHTML)?
				tex = calculo.find_element_by_tag_name("script").get_attribute("innerHTML")
		
				#WIP TeX - método #02
				#lista_split = calculo.text.split("\n")
				#tex = ("").join(lista_split)
		
				#mandar cada tex pra uma lista...
		
				resolucao_steps.append(tex)
		
				#print("indice = " + str(indice) + " --> " + tex)
				indice += 1
		
			#-------------------------

		if math_type == "mathml" :
				
				#DEBUG MathML
		
				mathml = codecs.encode(calculo.get_attribute("data-mathml") , 'utf-8')
				print("indice = " + str(indice) + " --> " + str(mathml))
				indice += 1
		#--------------------------

		
	#fim do for loop
	
	indice=0		

#fim de Resolucao()


def CorrigirResolucao(math_type):
	global resolucao_steps
	n = 0

	#funcao desnecessaria
	#so usar os pacotes certos no documento LaTeX
	#talvez eu use isso pra outra coisa...

	if math_type == "tex" :
	
	
		print("[DEBUG] CorrigirResolucao em tex")	
		#corrige o TeX obtido
		#lembre-se do caracter especial "\" - precisarei de dois
		#ler "correcoes_tex_capturado.txt"
		
		
		for i in range(0, len(resolucao_steps)):
			#print ("[DEBUG] i = " + str(i))
		
			#correcao #01
			#resolucao_steps[i] = resolucao_steps[i].replace("\\dfrac", "\\frac")
			#resolucao_steps[i] = resolucao_steps[i].replace("\\tfrac", "\\frac")
			#print ("[DEBUG] resolucao_steps[" + str(i) +"] = " + resolucao_steps[i])
		
			#correcao #02
			#parece que str.strip() come parte do texto
			#b = b.replace("\\class{steps-node}" , "")
			#resolucao_steps[i] = resolucao_steps[i].replace("\\class{steps-node}" , "")
			#resolucao_steps[i] = resolucao_steps[i].replace("{}" , "")
			#print ("[DEBUG] resolucao_steps[" + str(i) +"] = " + resolucao_steps[i])
		
			#usar re.sub()
			#b = re.sub(r"{.cssId", "" , b)
			#b = re.sub(r".steps-node-.\}", "" , b)
		
			#pega = re.subn(r"{.cssId", "" , resolucao_steps[i])
			#resolucao_steps[i] = pega[0]
			#print ("[DEBUG] resolucao_steps[" + str(i) +"] = " + resolucao_steps[i])
			#n += pega[1]
			#print("[DEBUG] n #01 = " + str(n))
		
			#pega = re.subn(r".steps-node-.\}", "" , resolucao_steps[i])
			#resolucao_steps[i] = pega[0]
			#print ("[DEBUG] resolucao_steps[" + str(i) +"] = " + resolucao_steps[i])
			#n += pega[1]
			#print("[DEBUG] n #02 = " + str(n))		
		
			#limpar "}" dos cssID
			#if n != 0 :
			#	resolucao_steps[i] = re.sub( "}", "" , resolucao_steps[i], count=n)
			#	print("[DEBUG] limpou o #" + str(i) + " " + str(n) + " vezes")
			#	
			#	#zerar a cada expressao
			#	n=0
			#
			#print ("[DEBUG] resolucao_steps[" + str(i) +"] = " + resolucao_steps[i])
			#print("\n")
		
		
			#correcao #03

			resolucao_steps[i] = "$$" + resolucao_steps[i] + "$$"
			
			#print ("[DEBUG] resolucao_steps[" + str(i) +"] = " + resolucao_steps[i])
			#print("\n")


		#fim do for loop 	

	#fim do if pro tex
	
	
	
	if math_type == "mathml" :
	
		print("[DEBUG] CorrigirResolucao em mathml")
	
	#fim do if pro mathml

#fim de CorrigirResolucao()


#apagar essa funcao depois
def Debug_MostraResolucao():
	global resolucao_steps
	
	print("\n[DEBUG] Debug_MostraResolucao()")
	
	for i in range(0, len(resolucao_steps)):
		print(resolucao_steps[i] + "\n")

	#fim do for loop   	




def Simplificar():
	global firefox

	# clicar em Simplify - mas precisa ser o de baixo
	simplify_list = firefox.find_elements_by_class_name('simplify-button')
	simplify_button = simplify_list[1]

	actions = ActionChains(firefox)
	actions.move_to_element(simplify_button)
	actions.click(simplify_button)
	actions.perform()

	print("[DEBUG] Simplify clicado!")


	# Esperar ate os calculos aparecerem...

	try:
			wait03 = WebDriverWait(firefox, timeout).until(
					EC.element_to_be_clickable((By.CLASS_NAME, "calc-content"))
			)

	finally:
			print("[DEBUG] Esperar antes de obter simplificação...")


	time.sleep(esperar)


	#capturar equacao simplificada

	#caso para "No Further Simplification Found"




	#--------------------


def Grafico():
	print("[DEBUG] Implementar Grafico()")



def ConstruirPagina(lista):
	
	pdf = None
	
	expressoes = "\n".join(lista)

	latex1 = r'''% Arquivo TeX para o Derivative-Calculator Bot de Rafael Requião
	\documentclass[12pt,a4paper]{memoir}      % Specifies the document class
	\usepackage{amsmath}
	%\usepackage[TS1,T1]{fontenc}
	\usepackage{textcomp}
	\newcommand {\class}[1]{ }       % mas dá erro de Undefined Control Sequence
	\newcommand {\cssId}[1]{ }
	\title{Selenium Derivative Calculator Bot}
	\author{Rafael Requiao}
	\date{March 15, 2018}
	\begin{document}
	\maketitle 
	\section{Questao 01}'''

	latex2 = r'''\end{document}               % End of document.'''

	#documento = []
	#documento = documento.append(latex1)
	#documento = documento.append(expressoes)
	#documento = documento.append(latex2)

	#latex = ("\n").join(documento)
	latex = latex1 + expressoes + latex2

	#debugging only
	#print(latex)

	# https://vog.github.io/texcaller/group__python.html

	pdf = texcaller.convert(latex, "LaTeX", "PDF", 5)

	nome_arquivo_pdf = "pdf.pdf"
	f_pdf = open(nome_arquivo_pdf , "wb")

	print(str(f_pdf))
	print(len(pdf))
	#print(str(pdf))

	pdf = pdf[0].encode("utf-8", "surrogateescape")
	#pdf = BytesIO(pdf)

	f_pdf.write(pdf)
	f_pdf.close()

	print("Escreveu PDF")



#fim de ConstruirPagina


def Exportar_TeX():
	print("[DEBUG] Implementar Exportar_TeX()")
	# criar documento de testes com expressoes no https://papeeria.com/
	


def Exportar_PDF():
	print("[DEBUG] Implementar Exportar_PDF()")
	


def Tchau():
	global firefox
	
	print("[DEBUG] Desligando...")
	time.sleep(esperar)
	firefox.quit()
	
#------------------------------------------

# Melhorias em tentativas de clicar em botões

def ClicarGo():

	global firefox

	try:
		go_button = firefox.find_element_by_id('go')

		actions = ActionChains(firefox)
		actions.move_to_element(go_button)
		actions.click(go_button)
		actions.perform()
		print("[DEBUG] Clicou em Go!")
		return True
	
	except:
		print("[DEBUG] Erro ao clicar em Go!")
		return False

#fim de ClicarGo()


def ClicarShowSteps():

	global firefox
		
	try:
		# Apertar "Show Steps"
		wait01 = WebDriverWait(firefox, timeout).until(

			#EC.presence_of_element_located((By.CLASS_NAME, "show-steps-button"))

			EC.element_to_be_clickable((By.CLASS_NAME, "show-steps-button"))
		)

	except:
		print("[DEBUG] Erro ao esperar Show Steps")
		return False
		

	finally:
		print("[DEBUG] Esperar antes de apertar Show Steps")
		time.sleep(3)


	print("[DEBUG] Tentar clicar em Show Steps!")


	try:
		#clicar em Show Steps
		
		#implementar pra no caso de 1 ou 2 Show Steps
		#testar expr = ln(1/x)
		
		show_steps_button = firefox.find_elements_by_class_name('show-steps-button')

		print("[DEBUG] show_step_button = " + str(show_step_button.text))
			
		actions = ActionChains(firefox)
		actions.move_to_element(show_steps_button)
		actions.click(show_steps_button)
		actions.perform()

		print("[DEBUG] Show Steps clicado!")
		return True

	except:
		print("[DEBUG] Erro ao clicar em Show Steps!")
		return False
	
	
#fim de ClicarShowSteps()	

#------------------------------------------

# ROTINA PRINCIPAL

#DEBUG selecionar modo
@click.command()
@click.option('--equation', prompt='Equation', help='Equation to convert')
@click.option('--format', type=click.Choice(output_formats), prompt='Output Format', help='Equation processing format')

def Fazer(equation, format):

	global bode
	global firefox
	
	
	expressao = equation
	math_type = format

	#Selecionar navegador - GeckoDriver (FIREFOX)!
	print("\n\nIniciando...\n\n")
	
	print("[DEBUG] webdriver.Firefox()")
	firefox = webdriver.Firefox(timeout=timeout, log_path="/tmp/geckolog.log")

	# setar tamanho legal pra visualizar a janela
	firefox.set_window_size(1280,720)
	print("[DEBUG] " + str(firefox.get_window_size()))
	#setar posicao da janela?


	#try:
	firefox.get('https://www.derivative-calculator.net/')


	#except TimeoutException:
	#	print("[DEBUG] Esperou a página carregar, mas deu timeout")


	print("[DEBUG] Carregou Pagina!")

	#seria bom diminuir o zoom da página?
	#enviar Ctrl + minus  3 vezes
	#mudar tecla, em caso de Mac ou Windows

	#Liberar INPUT do usuário
	#@click.command()
	#@click.option('--equation', prompt='Equation', help='Equation to convert')
	#@click.option('--iformat', type=click.Choice(input_formats), prompt='Input Format', help='Equation input format')


	# pegar o campo de busca onde podemos digitar algum termo
	campo_expressao = firefox.find_element_by_id('expression')

	#expressao = "ln(x/2)"

	# Digitar "Python Club" no campo de busca
	campo_expressao.send_keys(expressao)
	print("[DEBUG] Enviou expressao!")
	
	# Simular que o enter seja precisonado
	# ou seria melhor clicar em "GO!"
	
	#campo_expressao.send_keys(Keys.ENTER)
	#print("[DEBUG] Apertou ENTER!")
		
	#parece que clicar em qualquer coisa na tela, desbuga a view
	#implementar depois
	
	go = ClicarGo()
	
	if (go == True):
		print("[DEBUG] go = " + str(go))
		
		
	if (go == False):
		print("[DEBUG] go = " + str(go))
		ClicarGo()
	

	# Implementar Wait para identificar os botões depois de ter enviado expressão

	showsteps = ClicarShowSteps()
	
	if (showsteps == True):
		print("[DEBUG] showsteps = " + str(showsteps))
		
	if (showsteps == False):
		print("[DEBUG] showsteps = " + str(showsteps))
		showsteps = ClicarShowSteps()	


	# Esperar ate os calculos aparecerem...

	try:
			wait03 = WebDriverWait(firefox, timeout).until(
					EC.element_to_be_clickable((By.CLASS_NAME, "calc-content"))
			)

	except:
		print("[DEBUG] Erro ao esperar os calculos!")

	finally:
		print("[DEBUG] Esperar antes de obter calculos...")


	time.sleep(esperar)

	# Capturar dados de resultado para objeto Selenium
	#calculos_element = firefox.find_element_by_class_name("calc-content")
	#calculos_element = firefox.find_element_by_id("result")


	# Ajustar visualizacao

	#actions.move_to_element(calculos_element)
	#selenium.common.exceptions.MoveTargetOutOfBoundsException: 
	#Message: (824.5, 669.1583251953125) is out of bounds of viewport 
	#width (1280) and height (646)

	#definir elemento pra offset de posicao - ajeitar a view
	#guia_touch = firefox.find_element_by_id("result-text")

	#print("[DEBUG] Iniciar touch pra baixo...")
	#touch = TouchActions(firefox)
	#touch.scroll(0, -200)
	#touch.perform()

	#https://stackoverflow.com/questions/30937153/selenium-send-keys-what-element-should-i-use
	bode = firefox.find_element_by_xpath('//body')

	DesceJanelaUmPouco(7)

	#fim do for loop

	Resolucao(math_type)
	Debug_MostraResolucao() #comentar depois

	print("\n\n zzz \n\n")

	CorrigirResolucao(math_type)
	#Debug_MostraResolucao() #comentar depois

	#----------------------------------------------

	# Converter MathML pra TeX - incompleto/não usar
	# invocar o mathconverter do oerpub
	# Não... muito trabalho.
	# Só renderizar o MathML tá bom demais!
	# Usar benetech.github.io/mmlc-api

	#import requests, click

	#from lxml import etree


	# mathtype = "mathml"

	#-----------------------------------------------

  


	# obter simplificação
	#Simplificar()

	# obter gráfico
	#Grafico()

	# exportar tudo pra TeX e depois PDF
	#Exportar_TeX()

	#Exportar_PDF()

	print("[DEBUG] ConstruirPagina(resolucao_steps)")
	#time.sleep(3)

	ConstruirPagina(resolucao_steps)
	
	#abrir arquivo PDF
	os.system("open pdf.pdf")
	
	# desligar navegador
	Tchau()


#----------------------------------------

#fim de Fazer()

if __name__ == '__main__' :
	LimparTela()
	Fazer()






