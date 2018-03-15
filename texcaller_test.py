#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Teste de renderização de documento LaTeX com Python
# Criado por Rafael F S Requiao @ Python 3.6.4 (brew) - macOS 10.11

#----------------------------------------

from __future__ import division, print_function, unicode_literals

import texcaller

nome_arquivo_tex = "empty.tex"
f_tex = open(nome_arquivo_tex , "rb")

latex = f_tex.read() #talvez setar modo b
print("Leu TEX")

# https://vog.github.io/texcaller/group__python.html

pdf, info = texcaller.convert(latex, "LaTeX", "PDF", 5)

latex.close()

nome_arquivo_pdf = "pdf.pdf"
f_pdf = open(nome_arquivo_pdf , "wb")

f_pdf.write(pdf)
f_pdf.close()

print("Escreveu PDF")



