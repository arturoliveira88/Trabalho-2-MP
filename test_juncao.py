import os
from juncao import junta, gera_saida
from glob import glob
'''
path = './testes'

#arquivos = []

arquivos = sorted(glob(r'./testes/*.txt'))
'''


#saida_1 = open('T1saida.txt','r').read().split('\n').pop(-1)


def test_1():
    entrada = gera_saida(junta('./testes/T1A1.txt', './testes/T1A2.txt'))
    saida = open('T1saida.txt','r').read().split('\n')
    saida.pop()
    assert entrada == saida

'''
'./testes\T1A1.txt'   # pode-se usar esses caminhos como forma
'./testes\T1A2.txt'   # de se localizar o testes a serem abertos


for root, subFolder, filename in os.walk(path):
    for arquivo in filename:
        arquivos.append(open(arquivo, 'r'))
'''   

#print(junta(arquivos[0],arquivos[1]))

#print(junta('T1A1.txt','T1A2.txt'))