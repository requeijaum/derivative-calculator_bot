#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Criado por Rafael F S Requiao @ Python 3.6.4 (brew) - macOS 10.11


import os, sys, string, codecs

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

def clear_screen():
	os.system('cls' if os.name=='nt' else 'clear')
	
#----------------------------------------

clear_screen()

#Selecionar navegador - GeckoDriver (FIREFOX)!
print("[DEBUG] webdriver.Firefox()")
firefox = webdriver.Firefox(timeout=timeout, log_path="/tmp/geckolog.log")

# setar tamanho legal pra visualizar a janela
firefox.set_window_size(1280,720)
print(firefox.get_window_size())


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

#Parece que descer teclas buga tudo
print("[DEBUG] Descer a tela...")
for i in range(0,7) :
	bode.send_keys(u'\ue015')

#fim do for loop


print("[DEBUG] obter todos os div.calc-math e meter numa lista")

#try:
#calculos_element = 	firefox.find_elements_by_class_name(
#						"calc-math"
#					)

#calculos_element = 	firefox.find_elements_by_xpath(
#						#"//div[@class='calc-math']"  #TeX
#						"//span[@id='MathJax*']"
#					)
					
# DEBUG MathML
# limitar melhor o que aparece dentro daquele div.calc-math
# to pegando coisas de fora
calculos_element = 	firefox.find_elements_by_class_name("mjx-chtml")					
					
					
# Tratar elemento do Firefox antes de imprimir
					
#except:
#print("[DEBUG] erro... sem calc-math... :( ")



#pegar TeX de cada calc-math - element <script> ; type="math/tex"
indice=0
print("[DEBUG] print(MathML)")
for calculo in calculos_element:
		
		#DEBUG TeX
		#só existe o método .text na classe WebElement... pelo visto...
			
		#temp = codecs.encode(calculo.text , 'utf-8')
		#atributo1 = calculo.get_attribute("id")
		#atributo2 = calculo.get_attribute("type")
		#print("indice = " + str(indice) + " " + str(atributo1) + " " + str(atributo2) + " --> " + str(temp))
		
		#WIP TeX ?
		#lista_split = calculo.text.split("\n")
		#tex = ("").join(lista_split)
		#print("indice = " + str(indice) + " --> " + tex)
		
		#-------------------------
				
		#DEBUG MathML
		
		mathml = codecs.encode(calculo.get_attribute("data-mathml") , 'utf-8')
		print("indice = " + str(indice) + " --> " + str(mathml))

		indice += 1
		
#fim do for loop
		
indice=0

#----------------------------------------------

# Converter MathML pra TeX
# invocar o mathconverter do oerpub
# Não... muito trabalho.
# Só renderizar o MathML tá bom demais!
# Usar benetech.github.io/mmlc-api

import requests, click

from lxml import etree


# mathtype = "mathml"

def _call_mathml_cloud(equation, mathtype):
    """ the HTTP POST to MathMLCloud server """
    try:
        resp = requests.post('https://api.mathmlcloud.org/equation',
                             {'math': equation, 'mathType': mathtype, 'mml': 'true', 'description': 'true'})
        data = resp.json()
        try:
            mathml = data['components'][0]['source']
            return mathml
        except IndexError:
            # bug in MathML Cloud. It sometimes returns 200 but no result
            # (bummer).
            return 'null'
    except Exception, err:
        sys.stderr.write('MathML Cloud ERROR: %sn' % str(err))
        sys.exit(2)
        

        



print("[DEBUG] Desligando...")
time.sleep(esperar)
firefox.quit()
