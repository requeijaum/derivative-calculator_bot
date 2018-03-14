from selenium import webdriver
from selenium.webdriver.common.keys import Keys

firefox = webdriver.Firefox()
firefox.get('https://www.derivative-calculator.net/')

# pegar o campo de busca onde podemos digitar algum termo
campo_expressao = firefox.find_element_by_id('expression')

# Digitar "Python Club" no campo de busca
campo_expressao.send_keys('ln(x/2)')

# Simular que o enter seja precisonado
campo_expressao.send_keys(Keys.ENTER)
