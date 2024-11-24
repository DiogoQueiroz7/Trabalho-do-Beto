print('CALCULADORA DE FATORIAL RECURSIVA')
print('*********************************')

def fatorial(num):
    if num == 0:
        return 1 
    else:
        return num * fatorial(num - 1)
    
num = int(input('Digite um número para ser fatorado: '))

resultado = fatorial(num)

print(f'O resultado para fatorial de {num} é {resultado}')

print('******* FIM *******')