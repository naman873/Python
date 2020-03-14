def maze(board,c_r,c_c,t_r,t_c,row,col,hell=""):
     if c_r==t_r and c_c==t_c:
         print(hell)
         return

     if(c_r not in range(0,row)) or (c_c not in range(0,col)):
         return

     if board[c_r][c_c]:
         return

     board[c_r][c_c]=True
     maze(board,c_r-1,c_c,t_r,t_c,row,col,hell+"U")
     maze(board,c_r+1,c_c, t_r, t_c, row, col, hell + "D")
     maze(board, c_r, c_c-1, t_r, t_c, row, col, hell + "L")
     maze(board, c_r, c_c+1, t_r, t_c, row, col, hell + "R")
     board[c_r][c_c]=False


### Blockage


def mazeblock(board, c_r, c_c, t_r, t_c, row, col, hell=""):
    if c_r == t_r and c_c == t_c:
        print(hell)
        return

    if (c_r not in range(0, row)) or (c_c not in range(0, col)):
        return

    if board[c_r][c_c]:
        return

    board[c_r][c_c] = True
    mazeblock(board, c_r - 1, c_c, t_r, t_c, row, col, hell + "U")
    mazeblock(board, c_r + 1, c_c, t_r, t_c, row, col, hell + "D")
    mazeblock(board, c_r, c_c - 1, t_r, t_c, row, col, hell + "L")
    mazeblock(board, c_r, c_c + 1, t_r, t_c, row, col, hell + "R")
    board[c_r][c_c] = False


#board=[[False]*5 for i in range(3)]
#board[1][4]=True
#board[0][4]=True

### list of maze

def mazeblock_li(board, c_r, c_c, t_r, t_c, row, col, hell=""):
    if c_r == t_r and c_c == t_c:
        return[hell]

    if (c_r not in range(0, row)) or (c_c not in range(0, col)):
        return[]

    if board[c_r][c_c]:
        return[]

    acc=[]
    board[c_r][c_c] = True
    acc.extend(mazeblock_li(board, c_r - 1, c_c, t_r, t_c, row, col, hell + "U"))
    acc.extend(mazeblock_li(board, c_r + 1, c_c, t_r, t_c, row, col, hell + "D"))
    acc.extend(mazeblock_li(board, c_r, c_c - 1, t_r, t_c, row, col, hell + "L"))
    acc.extend(mazeblock_li(board, c_r, c_c + 1, t_r, t_c, row, col, hell + "R"))
    board[c_r][c_c] = False

    return acc

board=[[False]*5 for i in range(3)]
li=mazeblock_li(board,0,0,2,2,3,5)
sort=sorted(li,key=lambda item:len(item))
print(sort)
