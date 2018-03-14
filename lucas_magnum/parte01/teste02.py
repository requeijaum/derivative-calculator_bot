from selenium import webdriver

# Criar instância do navegador
firefox = webdriver.Firefox()

# Abrir a página do Python Club
firefox.get('http://pythonclub.com.br/')

# Seleciono todos os elementos que possuem a class post
posts = firefox.find_elements_by_class_name('post')

# Para cada post printar as informações
for post in posts:

    # O elemento `a` com a class `post-title`
    # contém todas as informações que queremos mostrar
    post_title = post.find_element_by_class_name('post-title')

    # `get_attribute` serve para extrair qualquer atributo do elemento
    post_link = post_title.get_attribute('href')

    informacoes = u"Titulo: {titulo}, \nLink: {link}"

    # printar informações
    print(informacoes.format(
      titulo=post_title.text,
      link=post_link
    ))

# Fechar navegador
firefox.quit()
