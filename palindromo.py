text = str(input('informe a palavra: '))

textreverse = text[::-1].lower()

if text.lower() == textreverse:
     print('Essa Frase e Palindromo')

else:
    print('Essa Frase não e Palindromo')

    

print(  f'Sua Frase {text} Reversa e {textreverse}')
print(textreverse)

