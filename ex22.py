print('CONTAGEM DE VOGAIS E CONSOANTES')
print('*******************************')

def contar(frase):
    lista_vogais = []
    lista_consoantes = []
    vogais = 'aeiou'
    consoantes =  'bcdfghjklmnpqrstuvwxyz'
    
    for letra in frase:
        if letra in vogais:
            lista_vogais.append(letra)
        elif letra in consoantes:
            lista_consoantes.append(letra)
        
    return (f' As consoantes são: {lista_consoantes} e a sua quantidade é {len(lista_consoantes)}, já as vogais são: {lista_vogais} e o seu número é: {len(lista_vogais)}')

frase = str(input('Digite uma frase para ser contado suas vogais e consoantes: ').lower())


resultado = contar(frase)
    
print(resultado)    
print('******* FIM *******')
    
    
    
    
    
    
    
