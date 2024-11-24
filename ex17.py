print('ORDENAÇÃO DE LISTA COM NÚMEROS NEGATIVOS E POSITVOS')
print('**************************************************')

def ordernar(lista_num):
    
    negativos = [num for num in lista_num if num < 0]
    positivos = [num for num in lista_num if num >= 0]
    lista_num_ordenada = negativos + positivos
    return f' A lista ordenada é: {lista_num_ordenada}'

lista_num = [5, -3, 12, -7, 8, -1, 0, 14, -6, 22, -13, 9, -4, 19, -2, 11, -8, 25, -10, 3]
print(f' A lista desordenada é: {lista_num}')
result = ordernar(lista_num)

print(result)