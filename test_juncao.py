import os
from juncao import junta, gera_saida

def test_1():  #Testando a junção e ordenação de dois arquivos sem repetição de numeros
    entrada = gera_saida(junta('./testes/T1A1.txt', './testes/T1A2.txt'))
    saida = open('./testes/T1saida.txt','r').read().split('\n')
    saida.pop()
    assert entrada == saida

def test_2(): #Testando a junção e ordenação de dois arquivos com todos os numeros repetidos
    entrada = gera_saida(junta('./testes/T2A1.txt', './testes/T2A2.txt'))
    saida = open('./testes/T2saida.txt','r').read().split('\n')
    saida.pop()
    assert entrada == saida