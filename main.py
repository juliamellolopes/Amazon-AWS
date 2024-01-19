# Desafio 1 (imprimir na tela "Ola Mundo")
print('Olá Mundo')

# Desafio 2 (declarar duas variaveis, uma chamada nome quue deve guardar o seu primeiro nome e a outa chamada idade
# deve guardar a sua idade como numero inteiro, depois deve imprmir na tela os dados)
first_name = 'Julia'
age  = '21'
print('Olá meu nome é', first_name, 'eu tenho', age, 'anos.')

# Desafio 3 (declare as variaveis num1 que deve guardar o numero 10 e num2 que deve guardar o numero de ponto flutuante 3.8
# depois imprima na tela o resultado de sua divisão )
num1 = 10
num2 = 3.8
resulte = num1/num2
print(resulte)

# Desfio 4 (crie um script que pergunte o nome e idade do usuário usando a funçao input() e depois imprima os dados)
first_name = input('Por favor, digite seu primeiro nome: ')
age = input('Agora, digite sua idade: ')
print('Olá {}, você tem {} anos'.format( first_name, age))

# Desafio 5 (crie um script que solicite ao usuáio dois numero e faça a soma, sibtração, exponencial e multiplicação deles)
num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
soma = num1+num2
subtracao = num1-num2
multiplicacao = num1*num2
exponenciacao = num1**num2
print(f'Soma: {soma}')
print(f'Subtração: {subtracao}' )
print(f'Multilicação: {multiplicacao}')
print(f'Exponenciação: {exponenciacao}')

# Desafio 6 (crie uma lista de chamada frutas, com os itens "mãça, banana, manga, e uva, depois imprima")
frutas = ['Maçã', 'Banana', 'Manga', 'Uva']
print(frutas)

# Desafio 7 (usando o anterior imprima o primeiro e o ultimo valor)
print(f'A primeira fruta é {frutas[0]}')
print(f'A ultima fruta é {frutas[-1]}')

# Desafio 8 (altere o segundo elemento da lista para morango, depoi adicione abacaxi na lista, depois imprima o resultado)
frutas[1] = "Morango"
frutas.append("Abacaxi")

# Desafio 9 (usando o desafio das frutas remova a manga usando remoce() depois o ultimo item da lista com o del
# por fim imprima)
frutas.remove('Manga')
del frutas[-1]

# Desafio 10 (faça um for loop para percorrer a lista e impriiir cada item)
for fruta in frutas:
    print('Eu gosto de '+ fruta)