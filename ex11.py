print('CONTADOR DE PALAVRAS ÚNICAS')
print('***************************')

def contador(frase):
    quantidade = set(frase.split(' '))
    return len(quantidade)

frase = str(input('Digite uma frase para ser contada: ').lower())
resultado = contador(frase)
print(f'A frase possui {resultado} palavras. ')

print('******* FIM *******')