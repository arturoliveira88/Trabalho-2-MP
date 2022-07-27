from juncao import junta, gera_saida

def test_1():
    entrada = gera_saida(junta('./testes/T1A1.txt', './testes/T1A2.txt'))
    saida = open('T1saida.txt','r').read().split('\n')
    saida.pop()
    assert entrada == saida
