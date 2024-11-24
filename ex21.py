print('REMOÇÃO DE ELEMENTOS DUPLICADOS')
print('********************************')

def remover_duplicados(lista):
    lista_sem_duplicatas = []
    vistos = set()
    
    for numero in lista:
        if numero not in vistos:
            lista_sem_duplicatas.append(numero)
            vistos.add(numero)
    
    return lista_sem_duplicatas

entrada = input('insira uma lista de números inteiros separados por espaços: ')
lista = list(map(int, entrada.split()))

print(f'A lista original é: {lista}')
lista_final = remover_duplicados(lista)
print(f'A lista sem duplicatas é: {lista_final}')

print('********** FIM **********')

