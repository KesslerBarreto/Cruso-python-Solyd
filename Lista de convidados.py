
'''O programa vai ler a quantidade de pessoas
que serão convidados. Após ler, irá perguntar
o nome dos convidados e vai criar uma lista e imprimir.'''

print('Programinha de controle de convidados 1.0')
print('###########################################')


numero_de_convidados = input('Coloque o numero de convidados: ')
lista_de_convidados = []


i= 1
while i <= int(numero_de_convidados) :
    nome_do_convidado = input('Coloque o nome do convidado : #'+str(i)+':  ' )
    lista_de_convidados.append(nome_do_convidado)
    i+=1

print('Serão', numero_de_convidados, 'convidados')
print('\nLISTA DE CONVIDADOS')

for convidado in lista_de_convidados:
    print(convidado)




