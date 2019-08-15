#Nome ao contario em maúscula


print('-----Pode Digitar seu nome com letras minúsculas----- ')

nome = input('Digite o seu nome, Por favor ')

for n in range(len(nome) -1 ,-1,-1):
    print(nome[n].upper(), end='')

'''
    len(nome) -1 significa que é a ultima letra da string
    -1 , começar a contar incluindo o zero
    -1, contagem decrescente '''


def cuber(num):
    num_cuber = num ** 3;
    return num_cuber

print(cuber(5))