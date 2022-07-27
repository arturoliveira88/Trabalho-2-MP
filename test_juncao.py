from juncao import junta, gera_saida

<<<<<<< HEAD
def test_1():  #Testando a junção e ordenação de dois arquivos sem repetição de numeros
=======
def test_1():
>>>>>>> 378b9cd13551b4d89010617fda2b56b3a3cff5a2
    entrada = gera_saida(junta('./testes/T1A1.txt', './testes/T1A2.txt'))
    saida = open('./testes/T1saida.txt','r').read().split('\n')
    saida.pop()
    assert entrada == saida
<<<<<<< HEAD

def test_2(): #Testando a junção e ordenação de dois arquivos com todos os numeros repetidos
    entrada = gera_saida(junta('./testes/T2A1.txt', './testes/T2A2.txt'))
    saida = open('./testes/T2saida.txt','r').read().split('\n')
    saida.pop()
    assert entrada == saida
=======
>>>>>>> 378b9cd13551b4d89010617fda2b56b3a3cff5a2
