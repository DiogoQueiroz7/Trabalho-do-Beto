print('VERIFICADOR DE ANAMAGRAMA')
print('*************************')

def verificar_anagrama(palavra1, palavra2):

    palavra1_ordenada = sorted(palavra1)
    palavra2_ordenada = sorted(palavra2)
    
    if palavra1_ordenada == palavra2_ordenada:
        return (f'As palavras {palavra1} e {palavra2} são um anagrama')
    else:
        return 'não é um anagrama'
    
    

palavra1 = str(input('Digite uma palavra para verificar se é anagrama: '))
palavra2 = str(input('Digite a segunda palavra para verificar: '))

resultado = verificar_anagrama(palavra1, palavra2)

print(resultado)

print('******* FIM *******')