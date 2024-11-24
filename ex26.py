print('MESCLAGEM DE DOIS DICIONARIOS')
print('*****************************')

def mesclar(dic1, dic2):
    
    dic3 = dic1.copy()
    for chave, valor in dic2.items():
        if chave in dic3:
            dic3[chave] += valor
        else: 
            dic3[chave] = valor
    return dic3

dic1 = {
    "nome": 'Diogo',
    "Sobrenome": 'Queiroz',
    "idade": 16
}
dic2 = {
    'idade': 4,
    'cor': 'pardo'
}

resultado = mesclar(dic1, dic2)

print(resultado)