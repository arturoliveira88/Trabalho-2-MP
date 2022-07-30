def junta(s1, s2):
    
    """
    Junta e ordena o conteudo de dois arquivos
    
    Argumentos:
        :s1: string referente ao arquivo 1
        :s2: string referente ao arquivo 2
        
    Retorna:
        :: Lista com os valores ordenados
    """
    
    A1 = open(s1, 'r')
    A2 = open(s2, 'r')
    
    lista_A1 = []
    lista_A2 = []
    
    for i in A1:
        i = i.rstrip()
        if '.' in i:
            lista_A1.append(float(i))
        else:
            lista_A1.append(int(i))
        
    for i in A2:
        i = i.rstrip()
        if '.' in i:
            lista_A1.append(float(i))
        else:
            lista_A2.append(int(i))
        
    lista_A1.extend(lista_A2)
    lista_A1.sort()
    return lista_A1

def gera_saida(lista):
    
    """
    Gera o arquivo resultante da função "junta(s1, s2)"
    
    Argumento:
        :lista: Recebe uma lista
        
    Retorna:
        :: Lista com valores em sring
    
    """
    
    
    
    with open('saida.txt','w') as arquivo:
        for i in lista:
            arquivo.write(str(i)+'\n')
            
    lista_str = []
    
    for i in lista:
        lista_str.append(str(i))
            
    return lista_str

