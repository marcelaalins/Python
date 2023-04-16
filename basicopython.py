# para entender como funciona python, é necessário uma breve explicação dos comandos básicos
print("imprime algo na sua tela")

#variáveis: atribui valor a algo

x = 223
print(x)

#entre aspas simples, ele imprime o que consta no parênteses
print('x')

#também imprime o que contém no parênteses em aspas duplas
print("x")

#criando outra variável e utilizando em cálculos

x = 34
y = 42

print(x,y)
print(x+y) #soma
print(x*y) #multiplicação
print(x**y) #elevação
print(x-y) #subtração
print(x/y) #divisão

#posso atribuir outro número a variável x ou y, ou adicionar outra variável

x = 56
y = 88
z = 9

print(x, y,z)
print(x+z) #soma
print(z*y) #multiplicação
print(x**z) #elevação
print(z-y) #subtração
print(x/z) #divisão

#operadores aritméticos:  adição (+), subtração (-), multiplicação (*), divisão (/) e exponenciação (**)

#estruturas condicionais: if and else, ifelse

idade = 43
if idade > 40:
    print("idade maior que 40")
    
#loop: serve para executar um bloco de código, ou seja, roda até que o resultado esperado apareça
#tipos de loop: loop for e loop while

#exemplo de loop for:
for i in range(1,5):
    print(i)

#por que o range não inclui todos os números, como o 5, nesse caso? essa função é chamada de built-in, retornando uma sequência de números
#por padrão, essa função começa por zero e incrementa até o número antes do último valor especificado
#os números são guardados como arrays, então quando solicitados, pegam a posição zero do range
#se eu pedir um range de (5), ele me retorna de 0 até 4, como array
#se eu pedir um intervalo de range, ele vai considerar que a primeira posição é o ponto de partida, como no exemplo printado acima
#é como se ele sempre considerasse o espaço que o número 0 ocupa
#no range(5) o zero vem automaticamente
#no range de intervalo range(1,5) ele corta o zero da visualização, mas ele ainda existe ocupando um espaço na memória
#o resultado deste último seria 1,2,3,4 (e o zero, só que não aparece na nossa tela)

#se eu cortar mais ainda o intervalo em que começará a contagem, menos números a função me retornará
for b in range(2,5):
    print(b)
#resultado: 2,3,4

#listas: utilizadas para manipular elementos

# Criação de uma lista
minha_lista = [1, 2, 3, 4, 5]

# Acesso aos elementos da lista
print(minha_lista[0]) #imprime 1, porque é primeira posição (a posição zero) na memória
print(minha_lista[-1]) #imprime 5, porque lê da direita para a esquerda

# Fatias de lista
print(minha_lista[1:3]) #imprime [2, 3]

# Adicionando elementos à lista
minha_lista.append(32782377) #append insere um registro após o último elemento listado
print(minha_lista) #imprime [1, 2, 3, 4, 5, 32782377]

# Removendo elementos da lista
minha_lista.remove(2) #remove o número 2 que constava na lista
print(minha_lista) #imprime [1, 3, 4, 5, 32782377]

# Ordenação de lista
minha_lista.sort()
print(minha_lista) #imprime [1, 2, 4, 5, 32782377]
