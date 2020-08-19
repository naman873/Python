def startDown(stars):

    if stars==0:
        return
    for i in range(stars):
        print("*",end='')
    print()
    startDown(stars-1)

#startDown(5)


def startup(stars):

    if stars==0:
        return
    startup(stars-1)
    for i in range(stars):
        print("*",end='')
    print()

#startup(5)


def starDownrec(row,col):
    if row<0:
        breakpoint(exit())

    if col==row:
        print()
        starDownrec(row-1,0)


    print("*",end='')
    starDownrec(row,col+1)

starDownrec(5,0)

