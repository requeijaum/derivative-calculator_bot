#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Criado por Rafael F S Requiao @ Python 3.6.4 (brew) - macOS 10.11


import os, sys, string, codecs, re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# implementar Wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# implementar interacao do teclado e mouse
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions

# implementar timeout handling
import time

from selenium.common.exceptions import TimeoutException
timeout = 20
esperar = 10

#----------------------------------------

# FUNÇÕES

def LimparTela():
	os.system('cls' if os.name=='nt' else 'clear')

#fim de LimparTela()


def DesceJanelaUmPouco(num):
	# Tirar bug caso o mouse clique em algum lugar fora da visualizacao
	# Parece que descer teclas buga tudo - foda-se
	print("[DEBUG] Descer a tela...")
	for i in range(0, num) :
		bode.send_keys(u'\ue015')

#fim de DesceJanelaUmPouco()


def Resolucao():
	global resolucao_steps
	
	print("[DEBUG] obter todos os div.calc-math e meter numa lista")

	try:
		calculos_element = 	firefox.find_elements_by_class_name(
								"calc-math"
							)

	#calculos_element = 	firefox.find_elements_by_xpath(
	#						#"//div[@class='calc-math']"  #TeX
	#						"//span[@id='MathJax*']"
	#					)
					

	# DEBUG MathML
	# limitar melhor o que aparece dentro daquele div.calc-math
	# to pegando coisas de fora
	#calculos_element = 	firefox.find_elements_by_class_name("mjx-chtml")					
					
					
	# Tratar elemento do Firefox antes de imprimir
					
	except:
		print("[DEBUG] erro... sem calc-math... :( ")



	#pegar TeX de cada calc-math - element <script> ; type="math/tex"
	indice=0
	resolucao_steps=[] #talvez mudar isso aqui pra outro lugar
	
	print("[DEBUG] print(tex)")
	#print("[DEBUG] print(MathML)")

	for calculo in calculos_element:
		
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
		
			#-------------------------
				
			#DEBUG MathML
		
			#mathml = codecs.encode(calculo.get_attribute("data-mathml") , 'utf-8')
			#print("indice = " + str(indice) + " --> " + str(mathml))
		
			#--------------------------
		
			indice += 1
		
	#fim do for loop
	indice=0		

#fim de Resolucao()


def CorrigirResolucao():
	global resolucao_steps
	n = 0
	
	#corrige o TeX obtido
	#lembre-se do caracter especial "\" - precisarei de dois
	#ler "correcoes_tex_capturado.txt"
	for i in range(0, len(resolucao_steps)):
		
		#correcao #01
		resolucao_steps[i] = resolucao_steps[i].replace("\\dfrac", "\\frac")
		resolucao_steps[i] = resolucao_steps[i].replace("\\tfrac", "\\frac")
		
		#correcao #02
		#parece que str.strip() come parte do texto
		#b = b.replace("\\class{steps-node}" , "")
		resolucao_steps[i] = resolucao_steps[i].replace("\\class{steps-node}" , "")
		resolucao_steps[i] = resolucao_steps[i].replace("{}" , "")
		
		#usar re.sub()
		
		#b = re.sub(r"{.cssId", "" , b)
		#b = re.sub(r".steps-node-.\}", "" , b)
		
		pega = re.subn(r"{.cssId", "" , resolucao_steps[i])
		resolucao_steps[i] = pega[0]
		n += pega[1]
		
		pega = re.sub(r".steps-node-.\}", "" , resolucao_steps[i])
		pega = re.subn(r"{.cssId", "" , resolucao_steps[i])
		resolucao_steps[i] = pega[0]
		n += pega[1]		
		
		#limpar "}" dos cssID
		print("[DEBUG] limpou o #" + str(i) + " " + str(n) + "vezes")
		resolucao_steps[i] = re.sub(r"\}", "" , resolucao_steps[i], count=n)
		
		#zerar a cada expressao
		n=0
		
		print("\n")
		
		#correcao #03
		#lolwut



	#fim do for loop 	


#fim de CorrigirResolucao()


#apagar essa funcao depois
def Debug_MostraResolucao():
	global resolucao_steps
	
	for i in range(0, len(resolucao_steps)):
		print(resolucao_steps[i] + "\n")

	#fim do for loop   	




def Simplificar():
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



def Exportar_TeX():
	print("[DEBUG] Implementar Exportar_TeX()")
	# criar documento de testes com expressoes no https://papeeria.com/
	


def Exportar_PDF():
	print("[DEBUG] Implementar Exportar_PDF()")



def Tchau():
	print("[DEBUG] Desligando...")
	time.sleep(esperar)
	firefox.quit()
	
#----------------------------------------

# VARIÁVEIS GLOBAIS

global resolucao_steps



#----------------------------------------

# PROGRAMA PRINCIPAL

LimparTela()

#Selecionar navegador - GeckoDriver (FIREFOX)!
print("[DEBUG] webdriver.Firefox()")
firefox = webdriver.Firefox(timeout=timeout, log_path="/tmp/geckolog.log")

# setar tamanho legal pra visualizar a janela
firefox.set_window_size(1280,720)
print(firefox.get_window_size())
#setar posicao da janela?



#try:
firefox.get('https://www.derivative-calculator.net/')


#except TimeoutException:
#	print("[DEBUG] Esperou a página carregar, mas deu timeout")


print("[DEBUG] Carregou Pagina!")

# pegar o campo de busca onde podemos digitar algum termo
campo_expressao = firefox.find_element_by_id('expression')

expressao = "ln(x/2)"

# Digitar "Python Club" no campo de busca
campo_expressao.send_keys(expressao)

# Simular que o enter seja precisonado
campo_expressao.send_keys(Keys.ENTER)

print("[DEBUG] Enviou expressao!")

#parece que clicar em qualquer coisa na tela, desbuga a view
#implementar depois


# Implementar Wait para identificar os botões depois de ter enviado expressão

try:
	# Apertar "Show Steps"
	wait01 = WebDriverWait(firefox, timeout).until(

		#EC.presence_of_element_located((By.CLASS_NAME, "show-steps-button"))

		EC.element_to_be_clickable((By.CLASS_NAME, "show-steps-button"))
	)

finally:
	print("[DEBUG] Esperar antes de apertar Show Steps")
	time.sleep(1)

print("[DEBUG] Saiu do finally!")


#clicar em Show Steps

show_steps_button = firefox.find_element_by_class_name('show-steps-button')

actions = ActionChains(firefox)
actions.move_to_element(show_steps_button)
actions.click(show_steps_button)
actions.perform()

print("[DEBUG] Show Steps clicado!")


# Esperar ate os calculos aparecerem...

try:
        wait03 = WebDriverWait(firefox, timeout).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "calc-content"))
        )

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

Resolucao()
Debug_MostraResolucao() #comentar depois

print("\n\n zzz \n\n")

CorrigirResolucao()
Debug_MostraResolucao() #comentar depois

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
Exportar_TeX()

Exportar_PDF()


# desligar navegador
Tchau()


