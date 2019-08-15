# Identificar quantidade de Vogais e consoantes em uma string
vogais = ["a","e","i","o","u"] + ['A','E', 'I','O','U']

string = input("Digite uma palavra:")

vogais_na_string = ''
consoantes_na_string = ''

for i in range(len(string)):
    if string[i] in vogais:
        vogais_na_string += string[i]
    else:
        consoantes_na_string += string[i]

print('Vogais: ' + vogais_na_string)
print('Consoantes: ' + consoantes_na_string)

