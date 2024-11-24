print('VERIFICADOR DE SUDOKU')
print('**********************')

def e_valido(tabuleiro):
    def verificar_grupo(grupo):
        grupo = [num for num in grupo if num != 0]
        return len(grupo) == len(set(grupo))
    
    for linha in tabuleiro:
        if not verificar_grupo(linha):
            return False
    
    for col in range(9):
        coluna = [tabuleiro[linha][col] for linha in range(9)]
        if not verificar_grupo(coluna):
            return False
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrade = []
            for linha in range(i, i + 3):
                for coluna in range(j, j + 3):
                    subgrade.append(tabuleiro[linha][coluna])
            if not verificar_grupo(subgrade):
                return False
    
    return True

tabuleiro_exemplo = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Tabuleiro de Sudoku:")
for linha in tabuleiro_exemplo:
    print(linha)

resultado = e_valido(tabuleiro_exemplo)
print(f'O tabuleiro de Sudoku é válido: {resultado}')
print('******* FIM *******')


