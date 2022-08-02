# Criando a Função
from numpy import number


def função():
    print('Ednaldo Pereira')

# Chamando a função
função()

# Argumentos de função 

def somar(num, num2):
    print(num * num2)

somar(5, 15)

# Atribuindo variáveis em funções

x = somar(1, 50)

# Função para descobrir se um número é par ou impar


def primo():
    for i in range(2, 50):
        if i % 2==0:
            print('é Par ')
        else:
             i % 2==1
             print('é impar')

primo()





