def rat(row,col):
    if row==0 and col==0:
        return 1
    acc=0
    if row>0:
        acc+=rat(row-1,col)
    if col>0:
        acc+=rat(row,col-1)
    return acc

##print(rat(5,5))

def ratDP(row,col,memory):
    if row==0 and col==0:
        return 1
    if memory.get((row,col)):
        return memory.get((row,col))

    acc=0
    if row>0:
        acc+=ratDP(row-1,col,memory)
    if col>0:
        acc+=ratDP(row,col-1,memory)
    memory[(row,col)]=acc

    return acc

print(ratDP(50,50,{}))