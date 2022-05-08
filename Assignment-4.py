def is_attack(i, j, board, N):
    for k in range(1, i):
        if(board[k][j] == 1):
            return True
    k = i-1
    l = j+1

    while (k>=1 and l<=N):
        if (board[k][l] == 1):
            return True
        k=k+1
        l=l+1
    k = i-1
    l = j-1

    while (k>=1 and l>=1):
        if (board[k][l] == 1):
            return True
        k=k-1
        l=l-1
        
    return False

def n_queen(row, n, N, board):
    if (n==0):
        return True
    for j in range(1, N+1):
        if(not(is_attack(row, j, board, N))):
            board[row][j] = 1
            if (n_queen(row+1, n-1, N, board)):
                return True
    
            board[row][j] = 0
    return False

if __name__ == '__main__':
    board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    n_queen(1, 4, 4, board)
    for i in range(1, 5):
        print(board[i][1:])