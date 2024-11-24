print('CALCULADORA SIMPLES')
print('*******************')

def somar(a, b):
    return(a + b)
a = int(input('Digite um número para ser somado: '))
b = int(input('Digite um segundo número para ser somado: '))
resultado = somar(a, b)

print(f'O resultado da sua conta é: {resultado}')
print('******* FIM *******')