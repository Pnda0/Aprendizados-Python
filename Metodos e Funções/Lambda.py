# Funções usando o result para criar uma função com conteúdos criados

def quadrado(number):
    result = number ** 2
    return result

print(quadrado(15))

# Reduzindo uma linha de código usando o return
def triangulo(number):
    return number * 2

print(triangulo(7))

# Função em Lambda, para otimizar a escrita em uma única linha

def cross(number): return number * 2

print(cross(10))

# Forma alternativa de definição de função usando o lambda

start = lambda num: num + 77

print(start(3))

# Testando se um número é par ou impar

par = lambda x: x % 2==0

print(par(35))

# lambda para pegar o primeiro caractere de uma string

texto = lambda x: x[0]

print(texto('EAI GALERINHA'))

# Invertendo uma string 

inverter = lambda s: s[8:]

print(inverter('Caralho tu conhece a Paolla?'))















