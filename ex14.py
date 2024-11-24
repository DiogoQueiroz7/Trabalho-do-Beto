print('VERIFICADOR DE PALÍNDROMOS')
print('**************************')

def palindromo(palavra):
    if palavra == palavra[::-1]:
        return f'A palavra {palavra} é um palíndromo'
    else:
        return f'A palavra {palavra}, não é um palíndromo'
    
palavra = str(input('Digite uma palavra para verificar se é palíndromo: ').lower())
resultado = palindromo(palavra)

print(resultado)

print('******* FIM *******')