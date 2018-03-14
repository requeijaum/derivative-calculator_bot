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
	wait01 = WebDriverWait(firefox, 10).until(

		#EC.presence_of_element_located((By.CLASS_NAME, "show-steps-button"))

		EC.element_to_be_clickable((By.CLASS_NAME, "show-steps-button"))
	)

finally:
	print("[DEBUG] Esperar antes de apertar Show Steps")
	wait02 = WebDriverWait(firefox, 5)
	show_steps_link = firefox.find_element_by_class_name('show-steps-button')


print("Funcionou?")
