# Percorra a string abaixo e se o comprimento de uma palavra for par imprima "é par"

st = 'Print only the words that start with s in this sentence'
spliter = st.split()

for i in spliter:
    size =len(i)
    if size % 2==0:
        print(i, "é par")

#Resposta: only é par, that é par, with é par, in é par, this é par, sentence é par.

