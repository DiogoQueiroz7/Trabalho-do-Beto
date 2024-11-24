print('GERADOR DE TABUADA')
print('******************')

def tabuada(num):
    resultados = []
    for i in range(1, 11):
        resultado = num * i
        resultados.append(f' A multiplicação do {num} * {i} é: {resultado}')
    return resultados

num = (int(input('Digite um número para a tabuada: ')))
resultados = tabuada(num)
for linha in resultados:
    print(f'{linha}')