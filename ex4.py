print('CONTADOR DE CARACTERES EM UMA PALAVRA')
print('*************************************')

def contador(palavra):
    qtd = (len(palavra))
    return qtd
palavra = (str(input('Digite uma palavra para ser contada: ')))
resultado = contador(palavra)

print(f'A quantidade de caracteres na sua palavra é de: {resultado}')