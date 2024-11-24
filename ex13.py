print('MÉDIA COM NOTAS MAIORES QUE A MÉDIA')
print('***********************************')

def notes(notas):
    notas_acima = []
    soma = sum(notas)
    qtd = (len(notas))
    media = soma / qtd
    
    notas_acima = [n for n in notas if n > media]
    return f'As notas que ficaram acima da média foram: {notas_acima}'


notas = list(map(float, input('Digite as notas dos alunos separadamente: ').split()))
resultado = notes(notas)

print(resultado)

print('******* FIM *******')