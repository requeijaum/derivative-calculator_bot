#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Teste de renderização de documento LaTeX com Python
# Criado por Rafael F S Requiao @ Python 3.6.4 (brew) - macOS 10.11

#----------------------------------------

from __future__ import division, print_function, unicode_literals
import tex, texcaller, io, codecs
from io import StringIO, BytesIO


nome_arquivo_tex = "empty.tex"
f_tex = open(nome_arquivo_tex , "r")

latex = f_tex.read() #talvez setar modo b
print("Leu TEX")
f_tex.close()

# https://vog.github.io/texcaller/group__python.html

pdf = texcaller.convert(latex, "LaTeX", "PDF", 5)

nome_arquivo_pdf = "pdf.pdf"
f_pdf = open(nome_arquivo_pdf , "wb")

print(str(f_pdf))
print(len(pdf))
#print(str(pdf))

pdf = pdf[0].encode("utf-8", "surrogateescape")
#pdf = BytesIO(pdf)

f_pdf.write(pdf)
f_pdf.close()

print("Escreveu PDF")



