def b(n):
    if n==0:
        return

    c=6
    c=c-n
    print(c)

    b(n-1)

b(5)