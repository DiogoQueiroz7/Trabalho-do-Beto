print('CALCULADORA DE ÁREA DE RETÂNGULO')
print('********************************')

def calcular(base, altura):
    area = base * altura / 2
    return area

base = float(input('Digite a base do seu retângulo: '))
altura = float(input('Digite a altura do seu retângulo: '))
resultado = calcular(base, altura)

print(f'A área do seu retângulo é de:  {resultado}')

print('******* FIM *******')