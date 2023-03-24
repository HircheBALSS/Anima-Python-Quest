def valid_solution(board):
    # Vérifier les lignes
    for row in board:
        if set(row) != set(range(1, 10)):
            return False
    
    # Vérifier les colonnes
    for col in range(9):
        if set([board[row][col] for row in range(9)]) != set(range(1, 10)):
            return False
    
    # Vérifier les carrés
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = [board[row][col] for row in range(i, i+3) for col in range(j, j+3)]
            if set(square) != set(range(1, 10)):
                return False
    
    return True