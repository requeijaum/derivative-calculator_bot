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

# implementar multiplas questoes na mesma janela

class Questao:
	"Uma questao com muitas coisas dentro"
	questoes_contador = 0

	#def __call__(self):
	#	return self

	def __init__(self, numero, questao, resolucao): #simplificacao, grafico, link, raizes)
		self.numero = numero
		self.questao = questao
		self.resolucao = resolucao
		Questao.questoes_contador += 1
		
	
	def contador(self):
		print("[DEBUG] Numero de questoes = " + Questao.questoes_contador)	
		

	def mostrar(self):
		print("questao = " + self.questao)
		print("numero = " + str(self.numero) + ", \nResolucao = " + self.resolucao + " \n")
		
#fim de class Questao()

#------------------------------------------

# VARIÁVEIS GLOBAIS

global repetir
repetir = 0

global resolucao_steps
global expressao
expressao = ""

global math_type
math_type = ""

#global input_formats = ['asciimath', 'latex', 'mathml']

global output_formats
output_formats = ['tex', 'mathml']

global bode
bode = None

global calculos_element
calculos_element = ""

global firefox
firefox = ""

global showsteps
showsteps = False

global go
go = False

global tratado
tratado = []

global q_list
q_list = []

#----------------------------------------

# FUNÇÕES


def LimparTela():
	os.system('cls' if os.name=='nt' else 'clear')

#fim de LimparTela()


def DesceJanelaUmPouco(num):
	global firefox

	#result = firefox.find_element_by_id("result-text")

	# Tirar bug caso o mouse clique em algum lugar fora da visualizacao
	# Parece que descer teclas buga tudo - foda-se
	print("[DEBUG] Descer a tela..." + str(num))
	'''
	for i in range(0, num) :
		actions = ActionChains(firefox)
		#actions.move_to_element(result)
		actions.click(result)
		actions.key_down(Keys.ARROW_DOWN)
		actions.perform()
	'''
	
	firefox.execute_script(window.scrollTo((document.body.scrollWidth/2),(document.body.scrollHeight)/4))
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

	nome_arquivo_pdf = ("").join(["pdf",str(i),".pdf"])
	f_pdf = open(nome_arquivo_pdf , "wb")

	#print(str(f_pdf))
	#print(len(pdf))
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
	global actions

	try:
		go_button = firefox.find_element_by_id('go')

		actions = ActionChains(firefox)
		actions.key_down(Keys.SPACE)
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

	global bode
	global firefox
	global actions
		
	#try:
	# Apertar "Show Steps"
	wait02 = WebDriverWait(firefox, timeout).until(
		#EC.presence_of_element_located((By.CLASS_NAME, "show-steps-button"))
		EC.element_to_be_clickable((By.CLASS_NAME, "show-steps-button"))
	)


	print("[DEBUG] Esperar antes de apertar Show Steps")
	time.sleep(5)

	#DesceJanelaUmPouco(2)
	
	actions = ActionChains(firefox)
	actions.send_keys(Keys.END + Keys.PAGE_UP + Keys.PAGE_UP)

	print("[DEBUG] Tentar clicar em Show Steps!")

	#clicar em Show Steps

	#implementar pra no caso de 1 ou 2 Show Steps
	#testar expr = ln(1/x)

	show_steps_button = None
	show_steps_button = firefox.find_element_by_class_name("show-steps-button")

	print("[DEBUG] --> show_step_button = " + str(show_steps_button))
	print("[DEBUG] --> show_step_button = " + str(show_steps_button.get_attribute("innerHTML")))
	
	actions = ActionChains(firefox)
	#actions.move_to_element(show_steps_button)
	actions.click(show_steps_button)
	actions.perform()

	print("[DEBUG] Show Steps clicado!")
	return True


	#except:
	#	print("[DEBUG] Erro ao clicar em Show Steps!")
	#	return False
				
			
#fim de ClicarShowSteps()	

#----------------=======================------------=================--------------


def IniciarNavegador():

	global bode
	global firefox

	

	#Selecionar navegador - GeckoDriver (FIREFOX)!
	print("\n\nIniciando...\n\n")

	#criar perfil
	bot_profile = webdriver.firefox.firefox_profile.FirefoxProfile(profile_directory="./profile/")
	
	bot_profile.set_preference("network.proxy.type", 1)
	bot_profile.set_preference("network.proxy.http", "127.0.0.1")
	bot_profile.set_preference("network.proxy.http.port", int(8080))
	bot_profile.update_preferences()
	
			
	print("[DEBUG] webdriver.Firefox()")
	firefox = webdriver.Firefox(firefox_profile=bot_profile, timeout=timeout, log_path="/tmp/geckolog.log")

	# setar tamanho legal pra visualizar a janela
	firefox.set_window_size(1440,900)
	print("[DEBUG] " + str(firefox.get_window_size()))
	#setar posicao da janela?


	#try:
	firefox.get('http://www.derivative-calculator.net/#expr=')
	#usando meu proxy

	#except TimeoutException:
	#	print("[DEBUG] Esperou a página carregar, mas deu timeout")

	print("[DEBUG] Carregou Pagina!")
	time.sleep(3)

	
	for i in range(0, 4) :  # seria melhor send_keys?
		html = firefox.find_element_by_xpath('//html')
		
		#diferença entre Mac e Windows
		#html.send_keys(Keys.CONTROL + Keys.SUBTRACT)
		#html.send_keys(Keys.COMMAND + Keys.SUBTRACT)
		
		#actions.key_down(Keys.CONTROL).key_down(Keys.SUBTRACT)
		#actions.perform()
		
		time.sleep(1)
		
		#actions.key_up(Keys.CONTROL).key_up(Keys.SUBTRACT)
		#actions.perform()
		
		#time.sleep(1)
		
	
	#firefox.execute_script()
	
	print("[DEBUG] Diminuir zoom da página - hack maravilhoso")
	
	bode = firefox.find_element_by_xpath('//html')


#fim de IniciarNavegador()

def AbrirArquivo():

	global tratado

	# abrir arquivo
	f = open("questoes_utf8.txt", "r", encoding="ascii")
	questoes = f.readlines()
	f.close()


	#tratar linhas em branco antes ou depois?
	for i in range(0, len(questoes)):
		if questoes[i] == "\n":
			print("")
		
		else:
			tratado.append(questoes[i].strip("\n"))	


	print("\n[DEBUG] " + str(tratado) + "\n\n")

#fim de AbrirArquivo()

def AbrirPDF():
	for i in  range(0, len(tratado)):
		#abrir arquivo PDF
		comando = ("").join(["open ","pdf",str(i),".pdf"])
		os.system(comando)


#------------------------------------------

# ROTINA PRINCIPAL

#DEBUG selecionar modo
#@click.command()
#@click.option('--equation', prompt='Equation', help='Equation to convert')
#@click.option('--format', type=click.Choice(output_formats), prompt='Output Format', help='Equation processing format')

def Fazer(i):

	global bode
	global firefox
	global showsteps
	global go
	global actions
	
	
	expressao = tratado[i]
	math_type = "tex"

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

	CLR = firefox.find_element_by_id('clear-expression-button')

	#apagar exrpessao anterior
	actions = ActionChains(firefox)
	actions.move_to_element(CLR).click(CLR).click(CLR).click(CLR).perform()
	
	#campo_expressao.send_keys(Keys.DELETE)
	
	#enviar expressao
	campo_expressao.send_keys(expressao)
	print("[DEBUG] Enviou expressao!")

	#https://stackoverflow.com/questions/30937153/selenium-send-keys-what-element-should-i-use
	#bode = firefox.find_element_by_xpath("//body")
	#print(str(bode))
	
	# Simular que o enter seja precisonado
	# ou seria melhor clicar em "GO!"
	
	#campo_expressao.send_keys(Keys.ENTER)
	#print("[DEBUG] Apertou ENTER!")
		
	#parece que clicar em qualquer coisa na tela, desbuga a view
	#implementar depois
	

	clicou_go    = 0
	clicou_steps = 0
	
	while (clicou_go < 3):
		go = ClicarGo()	
		clicou_go += 1
		
		if (go == True):
			clicou_go = 3
	
		print("[DEBUG] go = " + str(go))
		

	
	while (clicou_steps < 3):
		showsteps = ClicarShowSteps()
		clicou_steps += 1
			
		if (showsteps == True):
			clicou_steps = 3
	
		print("[DEBUG] showsteps = " + str(showsteps))


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
	#bode = firefox.find_element_by_xpath('//body')

	#DesceJanelaUmPouco(3)

	#fim do for loop

	Resolucao(math_type)
	#Debug_MostraResolucao() #comentar depois

	#print("\n\n zzz \n\n")

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

	print("\n[DEBUG] ConstruirPagina(resolucao_steps)")
	#time.sleep(3)
	ConstruirPagina(resolucao_steps)
	
	#abrir arquivo PDF
	#comando = ("").join(["open ","pdf",str(i),".pdf"])
	#os.system(comando)
	
	#rolar para o topo da página
	print("\n[DEBUG] rolar para o topo da página!\n")
	actions = ActionChains(firefox)
	#actions.move_to_element(show_steps_button)
	actions.click(firefox.find_element_by_class_name("calc-header"))
	actions.send_keys(Keys.HOME)
	actions.perform()
	


#----------------------------------------

#fim de Fazer()

if __name__ == '__main__' :

	LimparTela()
	IniciarNavegador()
	AbrirArquivo()
	
	for i in range(0, len(tratado)):
		Fazer(i)
	
	'''
		while (repetir == 0):
		
			try: 
				Fazer(i)
				repetir = 0
			
			except:
				print("[DEBUG] Fazer("+str(i)+") deu erro... repetindo")
				repetir = 1
	'''
	
	AbrirPDF()	
	Tchau()







