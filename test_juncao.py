import os
from juncao import junta, gera_saida

def test_1():  #Testando a junção e ordenação de dois arquivos sem repetição de números
    entrada = gera_saida(junta('./testes/T1A1.txt', './testes/T1A2.txt'))
    saida = open('./testes/T1saida.txt','r').read().split('\n')
    saida.pop()
    assert entrada == saida

def test_2(): #Testando a junção e ordenação de dois arquivos com todos os números repetidos
    entrada = gera_saida(junta('./testes/T2A1.txt', './testes/T2A2.txt'))
    saida = open('./testes/T2saida.txt','r').read().split('\n')
    saida.pop()
    assert entrada == saida
    
def test_3(): #Testando a junção e ordenação de dois arquivos com valores negativos
    entrada = gera_saida(junta('./testes/T3A1.txt', './testes/T3A2.txt'))
    saida = open('./testes/T3saida.txt','r').read().split('\n')
    saida.pop()
    assert entrada == saida
    
def test_4(): #Testando a junção e ordenação de dois arquivos com números decimais
    entrada = gera_saida(junta('./testes/T4A1.txt', './testes/T4A2.txt'))
    saida = open('./testes/T4saida.txt','r').read().split('\n')
    saida.pop()
    assert entrada == saida