# Criado por Rafael F S Requiao @ Python 3.6.4 (brew) - macOS 10.11

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


# melhorar screenshots
#https://stackoverflow.com/questions/15018372/how-to-take-partial-screenshot-with-selenium-webdriver-in-python

from PIL import Image
#from StringIO import StringIO
from io import StringIO, BytesIO

def capture_element(element,driver):

	print("[DEBUG] capture_element()")
	print(element.location)
	print(element.size)

	location = element.location
	size = element.size
		
	#img = driver.get_screenshot_as_png()
	img = bode.screenshot_as_png
	
	#testar objeto img
	
	#img = Image.open(StringIO(img))
	#Erro aqui --> TypeError: initial_value must be str or None, not bytes 
	#https://stackoverflow.com/questions/31064981/python3-error-initial-value-must-be-str-or-none
	
	imagem = Image.open(BytesIO(img))
	
	#arrendondar locations?
	
	left   = location['x']
	top    = location['y']
	right  = location['x'] + size['width']
	bottom = location['y'] + size['height']
	
	print(left)
	print(top)
	print(right)
	print(bottom)	

	#img.save("screenshot_original.png")
	#AttributeError: 'bytes' object has no attribute 'save'

	imagem.save("screenshot_uncropped.png")

	#https://w3c.github.io/webdriver/webdriver-spec.html#dfn-take-screenshot
	#não precisa fazer crop se não dá pra capturar a tela inteira...
	
	#tentar fazer crop do element body e depois cropar?
	
	imagem = imagem.crop((int(left), int(top), int(right), int(bottom)))
	
	#cropar de novo pra corrigir a cagada
	aeho   = int(top)
	aeho  += aeho/2
	print(aeho)
	
	#SystemError: tile cannot extend outside image
	imagem = imagem.crop((0, int(aeho), int(size['width']), int(size['height']) ))
	
	imagem.save('screenshot.png')
	



#fim da funcao capture_element()


#----------------------------------------

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


# Implementar Wait para identificar os botões depois de ter enviado expressão

try:
	# Apertar "Show Steps"
	wait01 = WebDriverWait(firefox, timeout).until(

		#EC.presence_of_element_located((By.CLASS_NAME, "show-steps-button"))

		EC.element_to_be_clickable((By.CLASS_NAME, "show-steps-button"))
	)

finally:
	print("[DEBUG] Esperar antes de apertar Show Steps")
	time.sleep(3)

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


time.sleep(10)

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
#print("[DEBUG] Descer a tela...")
#for i in range(0,7) :
#	bode.send_keys(u'\ue015')


#Verificar offset da pagina... nao to conseguindo tirar foto do que eu quero
#https://stackoverflow.com/questions/15018372/how-to-take-partial-screenshot-with-selenium-webdriver-in-python

#tirar_foto = "result"
#tirar_foto = "calc"

tirar_foto = "result"


calculos_element = firefox.find_element_by_id(tirar_foto)

print("[DEBUG] Achou elemento cuja id = " + tirar_foto + "")
print("[DEBUG] element.tag_name = " + calculos_element.tag_name )


# Tratar objeto Selenium antes de imprimir
#calculos = [x.calculos for x in calculos_element]

print("[DEBUG] Tirar screenshot do resultado...")
#calculos_element.screenshot("foo.png")

capture_element(calculos_element,firefox)


print("[DEBUG] Desligando...")
time.sleep(5)
firefox.quit()
