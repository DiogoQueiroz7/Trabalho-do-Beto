print('VERIFICADOR DE MAIORIDADE')
print('*************************')

def verificar(idade):
    if idade >= 18:
        return 'Você é maior de idade'
    else:
        return 'Você é menor de idade'

idade = (int(input('Informe a sua idade: ')))
resultado = verificar(idade)

print(resultado)