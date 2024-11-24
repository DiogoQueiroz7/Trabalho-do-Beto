print('GERADOR DE NÚMEROS NA SEQUÊNCIA FIBONACCI')

def gerar(num):
    anterior = 0
    proximo = 1
    soma = 1
    seq = [anterior, proximo]
    for n in range(2, num):
        soma = anterior + proximo
        anterior = proximo
        proximo = soma
        seq.append(soma)
        
    return seq

num = int(input('Digite um número para gerar a sequência fibonacci: '))
resultado = gerar(num)

print(resultado)

print('******* FIM *******')















