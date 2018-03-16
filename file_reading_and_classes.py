#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Leitura de arquivos e criação classes/objetos
# Criado por Rafael F S Requiao @ Python 3.6.4 (brew) - macOS 10.11

#----------------------------------------

from __future__ import division, print_function, unicode_literals
import tex, texcaller, io, codecs
from io import StringIO, BytesIO


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

q_list = []
tratado = []


#mock de resolucao
resolucoes = ["aehooo", "12345", "arco tg minha pica", "nao da pra ler", "typo errado"]


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


for obj in range(len(tratado)):
	obj = Questao(obj, tratado[obj], resolucoes[obj])
	q_list.append(obj)	


for i in range(0, len(tratado)):
	print(q_list[i].mostrar())


#EOF