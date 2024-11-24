print('NÚMEROS PRIMOS EM UM INTERVALO')
print('******************************')

def primos(inter1, inter2):
    primos = []
    for num in range(inter1, inter2+1):
        if num > 1:
            primo = True
            for i in range(2, num):
                if num % i == 0:
                    primo = False
                    break
        if primo:
            primos.append(num)
    return primos

inter1 = (int(input('Digite o íncio do intervalo que você quer saber se é primo: ')))
inter2 = (int(input('Digite o final do intervalo que você quer saber se é primo: ')))    

resultado = primos(inter1, inter2)
print(resultado) 

print('******* FIM *******')