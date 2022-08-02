# Use compreensão em listas para crair uma lista das primeiras letras de cada palavra na string abaixo:

st = 'Print only the words that start with s in this sentence'

spliter = st.split()

lista = [letter[0] for letter in spliter]
print(lista)
