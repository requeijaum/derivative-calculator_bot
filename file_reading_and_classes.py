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

	def __init__(self, numero, resolucao): #simplificacao, grafico, link, raizes)
		self.numero = numero
		self.resolucao = resolucao
		Questao.questoes_contador += 1
	
	def contarQuestoes(self):
		print("[DEBUG] Numero de questoes = " + Questao.questoes_contador)	


	def mostrarQuestao(self):
		print("[DEBUG] numero = " + self.numero + ", \nResolucao = " + self.resolucao + " \n")



#fim de class Questao()

f = open("questoes_utf8.txt", "r", encoding="ascii")
questoes = f.readlines()
f.close()

tratado = []

#tratar linhas em branco antes ou depois?
for i in range(0, len(questoes)):
	if questoes[i] == "\n":
		print("")
		
	else:
		tratado.append(questoes[i].strip("\n"))	


print(questoes)
print(tratado)

for i in range(0, len(tratado)):
		

