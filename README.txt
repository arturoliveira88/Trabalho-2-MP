TRABALHO 2 MP

Foram rodados 4 testes, cada um com um propósito. Os testes seguem a nomenclatura "T[numero do teste]A[numero do arquivo].txt",
por exemplo, T1A1.txt se refere ao Arquivo 1 do teste 1. Cada teste possui sua respectiva saída representada por 
"T[numero do teste]saida.txt".

Deve-se testar o programa digitando "pytest" no prompt de comando. Sempre que isso for feito será gerado um arquivo "saida.txt"
referente ao ultimo teste realizado.
 
Os testes estão armazenados na pasta "testes".

O primeiro teste foi feito com o objetivo de testar a junção e ordenação de dois arquivos sem repetição de números, sendo:

A1:
1
3
5
7
9

A2:
0
2
4
6
8

T1saida:
0
1
2
3
4
5
6
7
8
9

-------------------------------------------------------------------------------------------------

O segundo teste foi feito com o objetivo de testar a junção e ordenação de dois arquivos com todos os números repetidos, sendo:

A1:
1
2
3
4

A2:
4
3
2
1

T2saida:
1
1
2
2
3
3
4
4

-------------------------------------------------------------------------------------------------

O tereiro teste foi feito com o objetivo de testar a junção e ordenação de dois arquivos com valores negativos, sendo:

A1:
-3
-2
-1
0
3
2
1

A2:
10
-10
9
-9

T3saida:

-10
-9
-3
-2
-1
0
1
2
3
9
10

-------------------------------------------------------------------------------------------------

O quarto teste foi feito com o objetivo de testar a junção e ordenação de dois arquivos números decimais, sendo:

A1:
0.5
6.4
10.0
10.1

A2:
-0.5
-5.5
0
10.1
20

T4saida:
-5.5
-0.5
0
0.5
6.4
10.0
10.1
10.1
20
