# Criado por Rafael F S Requiao

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# implementar Wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Selecionar navegador - GeckoDriver (FIREFOX)!
firefox = webdriver.Firefox()
firefox.get('https://www.derivative-calculator.net/')


# pegar o campo de busca onde podemos digitar algum termo
campo_expressao = firefox.find_element_by_id('expression')

# Digitar "Python Club" no campo de busca
campo_expressao.send_keys('ln(x/2)')

# Simular que o enter seja precisonado
campo_expressao.send_keys(Keys.ENTER)


# Implementar Wait para identificar os botões depois de ter enviado expressão

try:
	# Apertar "Show Steps"
	wait01 = WebDriverWait(firefox, 3).until(
		EC.presence_of_element_located((By.class, "show-steps-button"))
	)
	show_steps_link = firefox.find_element_by_class_name('show-steps-button')

