from random import randint

print('SOMA DE DIAGONAIS DE UMA MATRIZ QUADRADA')
print('****************************************')

def matriz(tamanho):
    matrizes = []
    if tamanho > 0:
        for i in range(tamanho):
            linhas = []
            for j in range(tamanho):
                numeros = randint(1, 50)
                linhas.append(numeros)
            matrizes.append(linhas)
    soma_principal = 0
    soma_secundaria = 0
    
    for i in range(tamanho):
        soma_principal += matrizes[i][i]
        soma_secundaria += matrizes[i][tamanho - i - 1]
    
    print('A sua matriz é:')
    for linha in matrizes:
        print(linha)
        
    return f'A soma de sua diagonal principal é {soma_principal}, e de sua diagonal secundária é {soma_secundaria}'
    
tamanho = int(input('Digite um número para definir a dimensão da sua matriz: '))

resultado = matriz(tamanho)
print(resultado)

print('******** FIM ********')
