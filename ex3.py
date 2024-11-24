print('CONVERSOR DE TEMPERATURA')
print('***********************')

def conversor(temp):
    F = temp * 1.8 + 32
    return F

temp = int(input('Digite a temperatura em celsius para ser convertida em fahrenheit: '))
resultado = conversor(temp)

print(f'A sua temperatura em Fahrenheit é {resultado}')