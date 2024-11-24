print('CALCULO DE MÉDIA ARITMÉTICA')
print('***************************')

def calcular(not1, not2, not3):
    soma = not1 + not2 + not3
    resultado = soma / 3
    return f'A média aritmetica das notas {not1}+{not2}+{not3} é igual a {resultado}'

not1= float(input('Digite sua primeira nota: '))
not2 = float(input('Digite sua segunda nota: '))
not3 = float(input('Digite sua terceira nota: '))
resultado = calcular(not1, not2, not3)
print(resultado)

print('******* FIM *******')