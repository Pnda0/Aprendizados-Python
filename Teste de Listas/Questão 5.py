# Escreva um programa que imprima os números inteiros de 1 a 100. Para múltiplos de três imprima "Fizz"
# Para múltiplos de cinco, imprima "Buzz"
# E múltiplos de 3 e 5, imprima "FizzBuzz"



for i in range(1, 100):
    if i % 3==0 and i % 5==0:
        print( "FizzBuzz")
    elif i % 3==0:
        print("Fizz")
    elif i % 5==0:
        print("Buzz")
    else:
        print(i)

