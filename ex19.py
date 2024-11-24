print('CONTADOR DE CARACTERES DE UMA FRASE')
print('************************************')

def contador(frase):
    
    dicionario = {}
    for caractere in frase:
        if caractere in dicionario:
            dicionario [caractere] += 1
        else:
            dicionario [caractere] = 1
    return dicionario
frase = input('Digite uma frase para ser contado a qaunatidade de caracteres: ').lower()
resultado = contador(frase)
print(resultado)

print('******* FIM *******')