import numpy as np

def suduku(board,row=0,col=0):
    if row==9:
        print(board)
        return
    if col==9:
        suduku(board,row+1,0)
        return
    if board[row,col]!=0:
        suduku(board,row,col+1)
        return
    else:
        for item in range(1,10):
            if isSafe(board,row,col,item):
                board[row,col]=item
                suduku(board,row,col+1)
                board[row,col]=0
    return


def isSafe(board,row,col,item):

    if item in board[row,:]:
        return False

    if item in board[:,col]:
        return False

    row_c=row-(row % 3)
    col_c=col-(col % 3)
    cut=board[row_c:row_c+3,col_c:col_c+3]
    acc=np.array(cut)
    if item in acc.flatten():
        return False

    return True


### List



def suduku(board,row=0,col=0):
    if row==9:
        return [board.copy()]

    if col==9:
        return suduku(board,row+1,0)

    if board[row,col]!=0:
        return suduku(board,row,col+1)

    else:
        ac=[]
        for item in range(1,10):
            if isSafe(board,row,col,item):
                board[row,col]=item
                ac.extend(suduku(board,row,col+1))
                board[row,col]=0
    return ac


def isSafe(board,row,col,item):

    if item in board[row,:]:
        return False

    if item in board[:,col]:
        return False
    row_c=row-(row % 3)
    col_c=col-(col % 3)
    cut=board[row_c:row_c+3,col_c:col_c+3]
    acc=np.array(cut)
    if item in acc:
        return False

    return True




hell=[[0, 0, 0, 0, 0, 8, 4, 0, 0],
                      [5, 2, 0, 0, 0, 0, 0, 0, 0],
                      [0, 8, 7, 0, 0, 0, 0, 3, 1],
                      [0, 0, 3, 0, 1, 0, 0, 8, 0],
                      [9, 0, 0, 8, 6, 3, 0, 0, 5],
                      [0, 5, 0, 0, 9, 0, 6, 0, 0],
                      [1, 3, 0, 0, 0, 0, 2, 5, 0],
                      [0, 0, 0, 0, 0, 0, 0, 7, 4],
                      [0, 0, 5, 2, 0, 6, 3, 0, 0]]
arr=np.array(hell)

print(suduku(arr))