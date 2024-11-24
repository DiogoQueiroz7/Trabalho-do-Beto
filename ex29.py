print('REMOÇÃO DE ELEMENTOS DUPLICADOS DE UMA LISTA ANINHADA')
print('****************************************************')

def remover_duplicados(lista_aninhada):
    lista_sem_duplicatas = []
    for sublista in lista_aninhada:
        sublista_unica = list(set(sublista))
        lista_sem_duplicatas.append(sublista_unica)
    return lista_sem_duplicatas

num_sublists = int(input('Quantas sublistas você deseja inserir? '))

lista_aninhada = []
for _ in range(num_sublists):
    sublista = input('Digite os elementos da sublista, separados por espaços: ').split()
    sublista = list(map(int, sublista))  
    lista_aninhada.append(sublista)

resultado = remover_duplicados(lista_aninhada)

print('A lista original é:')
for sublista in lista_aninhada:
    print(sublista)

print('A nova lista sem duplicatas é:')
for sublista in resultado:
    print(sublista)

print('********** FIM **********')
