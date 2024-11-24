print('FILTRO DE NÚMEROS PARES')
print('***********************')

def filtrar(numeros):
    num_pares = []
    for num in numeros:
        if num % 2 == 0:
            num_pares.append(num) 
    return (f'Dos números que foram digitados, são pares = {num_pares}')
    
numeros = list(map(int,input('Digite números inteiros para receber apenas os pares, separados por espaço: ').split(' ')))

resultado = filtrar(numeros)

print(resultado)

print('******* FIM *******')
    
