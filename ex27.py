print('CONTADOR DE PALAVRAS FREQUENTES')
print('*******************************')

def contar(texto):

    texto = texto.lower()
    for carac in texto:
        if carac in '.,:!?;':
            texto = texto.replace(carac, ' ')
            
    dic_palavras = {}
    palavras = texto.split()
    
    for palavra in palavras:
        if palavra in dic_palavras:
            dic_palavras[palavra] += 1
        else:
            dic_palavras[palavra] = 1
            
    ordenadas = sorted(dic_palavras.items(), key=lambda item: item[1], reverse = True)[:5]
    
    return f' As palavras que mais se repetem no texto são: {ordenadas}'


texto = input('Digite um texto para ser contado as palavras mais frequentes dele: ')
resultado = contar(texto)

print(resultado)
            
print('******* FIM *******') 











