# coding: utf-8
from bs4 import BeautifulSoup

with open('./lista.html') as listafile:
    listahtml = BeautifulSoup(listafile.read(), 'html5lib')

lista = next(paragraph for paragraph in listahtml.find_all('p') if '666' in paragraph.text)
names = ['1. ' + name.split('. ')[1] for name in lista.strings]

with open('vagabundos.md', 'w') as vagabundofile:
    vagabundofile.write('\n'.join(names))
