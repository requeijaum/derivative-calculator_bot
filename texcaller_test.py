#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Teste de renderização de documento LaTeX com Python
# Criado por Rafael F S Requiao @ Python 3.6.4 (brew) - macOS 10.11

#----------------------------------------

from __future__ import division, print_function, unicode_literals
import tex, texcaller, io, codecs
from io import StringIO, BytesIO


#nome_arquivo_tex = "empty.tex"
#f_tex = open(nome_arquivo_tex , "r")

#latex = f_tex.read() #talvez setar modo b
#print("Leu TEX")
#f_tex.close()

lista = []
lista = [

r"$$\arctan\left(\sqrt{\ln\left(\tan\left(5x-1\right)\right)}\right)$$",

r"$$\class{steps-node}{\cssId{steps-node-1}{\tfrac{\mathrm{d}}{\mathrm{d}x}\left[\arctan\left(\sqrt{\ln\left(\tan\left(5x-1\right)\right)}\right)\right]}}$$",

r"$$=\class{steps-node}{\cssId{steps-node-2}{\dfrac{1}{\left(\sqrt{\ln\left(\tan\left(5x-1\right)\right)}\right)^2+1}}}\cdot\class{steps-node}{\cssId{steps-node-3}{\tfrac{\mathrm{d}}{\mathrm{d}x}\left[\sqrt{\ln\left(\tan\left(5x-1\right)\right)}\right]}}$$",

r"$$=\dfrac{\class{steps-node}{\cssId{steps-node-4}{\frac{1}{2}}}\class{steps-node}{\cssId{steps-node-5}{\ln^{\frac{1}{2}-1}\left(\tan\left(5x-1\right)\right)}}\cdot\class{steps-node}{\cssId{steps-node-6}{\tfrac{\mathrm{d}}{\mathrm{d}x}\left[\ln\left(\tan\left(5x-1\right)\right)\right]}}}{\ln\left(\tan\left(5x-1\right)\right)+1}$$",

r"$$=\dfrac{\class{steps-node}{\cssId{steps-node-7}{\frac{1}{\tan\left(5x-1\right)}}}\cdot\class{steps-node}{\cssId{steps-node-8}{\tfrac{\mathrm{d}}{\mathrm{d}x}\left[\tan\left(5x-1\right)\right]}}}{2\sqrt{\ln\left(\tan\left(5x-1\right)\right)}\left(\ln\left(\tan\left(5x-1\right)\right)+1\right)}$$",

r"$$=\dfrac{\class{steps-node}{\cssId{steps-node-9}{\sec^2\left(5x-1\right)}}\cdot\class{steps-node}{\cssId{steps-node-10}{\tfrac{\mathrm{d}}{\mathrm{d}x}\left[5x-1\right]}}}{2\tan\left(5x-1\right)\sqrt{\ln\left(\tan\left(5x-1\right)\right)}\left(\ln\left(\tan\left(5x-1\right)\right)+1\right)}$$",

r"$$=\dfrac{\class{steps-node}{\cssId{steps-node-11}{\left(5\cdot\class{steps-node}{\cssId{steps-node-13}{\tfrac{\mathrm{d}}{\mathrm{d}x}\left[x\right]}}+\class{steps-node}{\cssId{steps-node-12}{\tfrac{\mathrm{d}}{\mathrm{d}x}\left[-1\right]}}\right)}}\sec^2\left(5x-1\right)}{2\tan\left(5x-1\right)\sqrt{\ln\left(\tan\left(5x-1\right)\right)}\left(\ln\left(\tan\left(5x-1\right)\right)+1\right)}$$",

r"$$=\dfrac{\left(5\cdot\class{steps-node}{\cssId{steps-node-14}{1}}+\class{steps-node}{\cssId{steps-node-15}{0}}\right)\sec^2\left(5x-1\right)}{2\tan\left(5x-1\right)\sqrt{\ln\left(\tan\left(5x-1\right)\right)}\left(\ln\left(\tan\left(5x-1\right)\right)+1\right)}$$",

r"$$=\dfrac{5\sec^2\left(5x-1\right)}{2\tan\left(5x-1\right)\sqrt{\ln\left(\tan\left(5x-1\right)\right)}\left(\ln\left(\tan\left(5x-1\right)\right)+1\right)}$$"


]


expressoes = "\n".join(lista)


latex1 = r'''% Arquivo TeX para o Derivative-Calculator Bot de Rafael Requião
\documentclass[12pt,a4paper]{memoir}      % Specifies the document class
\usepackage{amsmath}
%\usepackage[TS1,T1]{fontenc}
\usepackage{textcomp}
\newcommand {\class}[1]{ }       % mas dá erro de Undefined Control Sequence
\newcommand {\cssId}[1]{ }
\title{Selenium Derivative Calculator Bot}
\author{Rafael Requiao}
\date{March 15, 2018}
\begin{document}
\maketitle 
\section{Questao 01}'''

latex2 = r'''\end{document}               % End of document.'''

#documento = []
#documento = documento.append(latex1)
#documento = documento.append(expressoes)
#documento = documento.append(latex2)

#latex = ("\n").join(documento)
latex = latex1 + expressoes + latex2

print(latex)

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



