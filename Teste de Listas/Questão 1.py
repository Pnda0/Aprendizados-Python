st = 'Print only the words that start with s in this sentence'

# Comando Split faz com que o python separe o texto por palavras
split = st.split()
print(split)


# Encontrando palavras com letras específicas

for letra in split:
    if letra[0] == 's': 
        print(letra)


# Ex 2:
for letra in split:
    if letra[0] == 't': 
        print(letra)

#Ex 2: the, that,this.


