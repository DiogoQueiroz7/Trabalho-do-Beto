print('CALCULADORA BÁSICA COM ESTRUTURAS CONDICIONAIS')
print('**********************************************')

def calcular(num1, num2, opr):
    if opr == '+':
        adc = num1 + num2 
        return f'A adição dos números {num1} + {num2} é igual a: {adc}'
    elif opr == '-':
        sub = num1 - num2
        return f'A subtração dos números {num1} - {num2} é igual a: {sub}'
    elif opr == '*':
        mult = num1 * num2
        return f'A multiplicação dos números {num1} * {num2} é igual a: {mult}'
    elif opr == '/':
        if num2 != 0:
            div = num1 / num2
            return f'A divisão dos números {num1} / {num2} é igual a: {div}'
        else:
            return 'Divisão por 0 não é válida'
    else:
        return 'Você não digitou uma operação válida'

num1 = float(input('Digite o primeiro número para a operação: '))

opr = input('Agora digite qual operação você quer: [+] [-] [*] [/]: ').lower()

num2 = float(input('Digite o segundo número para a operação: '))

resultado = calcular(num1, num2, opr)
print(resultado)
print('******* FIM *******')
