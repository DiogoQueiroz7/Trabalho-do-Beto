from random import randint

print('JOGO DE ADVINHAÇÃO')
print('******************')

def jogar(inicio, fim):
    numero = randint(inicio, fim)
    tentativa = 0
    acertou = False
    while not acertou:
        chute = int(input('Digite um número: '))
        if chute == numero:
            tentativa += 1
            acertou = True
            return f"Você acertou o número secreto que era {numero} e o seu número de tentativass foram de {tentativa} tentativas."
        elif chute > numero:  
            print('O número secreto é menor que esse, tente novamente!')
            tentativa += 1
        elif chute < numero: 
            print('O número secreto é maior que esse, tente novamente!')
            tentativa += 1

inicio = 1
fim = 100    
resultado = jogar(inicio, fim)
print(resultado)

print('******* FIM *******')