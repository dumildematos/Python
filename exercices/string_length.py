#Tamanho de  Strings
text1 = input('Introduza o primeiro texto ')
text2 = input('Introduza o segundo texto ')

print('O tamanho ' , text1 , ':' , len(text1) , 'Carateres')
print('O tamanho ' , text2 , ':' , len(text2) , 'Carateres')

if(len(text1) != len(text2)):
    print('As duas são diferentes')
elif(len(text1) == len(text2)):
    print('Os textos são iguais')
