def is_safe(x, y, n, board):
    """Verifica se a posição (x, y) é segura para o cavalo."""
    return 0 <= x < n and 0 <= y < n and board[x][y] == 0

def print_solution(board):
    """Imprime a solução do tabuleiro."""
    for row in board:
        print(" ".join(str(cell) for cell in row))
    print()

def solve_knights_tour(n):
    """Inicializa o tabuleiro e inicia a tentativa do passeio do cavalo."""
    # Tabuleiro n x n
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    # Movimentos possíveis do cavalo
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    
    # Inicializa a posição inicial do cavalo
    board[0][0] = 1  # Começa na posição (0, 0)
    
    # Tenta o passeio
    if not knights_tour_util(1, 0, 0, board, move_x, move_y, n):
        print("Não há solução")
    else:
        print_solution(board)

def knights_tour_util(step_count, curr_x, curr_y, board, move_x, move_y, n):
    """Função recursiva para tentar o passeio do cavalo."""
    if step_count == n * n:
        return True  # Todos os passos foram feitos

    for i in range(8):
        next_x = curr_x + move_x[i]
        next_y = curr_y + move_y[i]
        
        if is_safe(next_x, next_y, n, board):
            board[next_x][next_y] = step_count + 1  # Registra o movimento
            
            if knights_tour_util(step_count + 1, next_x, next_y, board, move_x, move_y, n):
                return True
            
            board[next_x][next_y] = 0  # Apaga o movimento (backtrack)

    return False  # Não encontrou uma solução

# Exemplo de uso
n = 5  # Tamanho do tabuleiro
solve_knights_tour(n)