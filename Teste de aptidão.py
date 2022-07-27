
''' Teste de Aptidão - Para ser apto é necessário
ter mais ou igual a  18 anos, 1.75 ou igual de altura,
 ter mais ou igual a 60 kg. '''


idade = int(input('Escreva sua idade: '))
altura = float(input('Esceva sua altura: '))
peso = float(input('Escreva seu peso: '))


if idade >= 18 and peso >= 60 and altura >= 1.75:
    print('Você está apto')
else:
    print('Você não está apto')




