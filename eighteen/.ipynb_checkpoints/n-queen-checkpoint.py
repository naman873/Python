def queen(board,row,n):
    if row == n:
        print("solution found")
        return

    for col in range(0,n):
        if isSafe(board,row,col,n):
            board[row][col]= True
            queen(board,row+1,n)
            board[row][col]=False

def isSafe(board,row,col,n):

    for step in range(1,row+1):

        if row-step>=0:

            if board[row-step][col]:
                return False

            if col-step>=0:
                if board[row-step][col-step]:
                    return False

            if col+step<n:
                if board[row-step][col+step]:
                    return False

    return True


board=[[False]*9 for i in range(9)]
queen(board,0,9)
