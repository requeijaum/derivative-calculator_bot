from selenium import webdriver
from selenium.webdriver.common.keys import Keys

firefox = webdriver.Firefox()
firefox.get('http://google.com.br/')

# pegar o campo de busca onde podemos digitar algum termo
campo_busca = firefox.find_element_by_name('q')

# Digitar "Python Club" no campo de busca
campo_busca.send_keys('Python Club')

# Simular que o enter seja precisonado
campo_busca.send_keys(Keys.ENTER)
