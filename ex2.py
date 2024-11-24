print('VERIFICADOR DE NÚMERO PAR OU ÍMPAR')
print('**********************************')

def verificador(num):
    if num % 2 == 0:     
        return('par') 
    else:
        return('ímpar')

num = int(input('Digite um número para verificar se é par ou ímpar: '))

resultado = verificador(num)
print(f'O número digitado é {resultado}')

print('******* FIM *******')