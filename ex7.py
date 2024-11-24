print('INVERSOR DE STRING')
print('******************')

def inversor(palavra):
    return palavra[::-1]

palavra = str(input('Digite uma palavra para ser invertida: ').lower())
resultado = inversor(palavra)

print(f' A sua palavra invertida é {resultado}')

print('******* FIM *******')