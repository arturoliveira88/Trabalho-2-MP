def junta(s1, s2):    #junta e ordena o conteudo de dois arquivos
    A1 = open(s1, 'r')
    A2 = open(s2, 'r')
    
    lista_A1 = []
    lista_A2 = []
    
    for i in A1:
        i = i.rstrip()
        lista_A1.append(i)
        
    for i in A2:
        i = i.rstrip()
        lista_A2.append(i)
        
    lista_A1.extend(lista_A2)
    lista_A1.sort()
    return lista_A1

def gera_saida(lista):
    with open('T1saida.txt','w') as arquivo:
        for i in lista:
            arquivo.write(str(i)+'\n')
            
    return lista

#print(junta('T1A1.txt','T1A2.txt'))