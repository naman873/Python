def fibo(n):
    if n<2:
        return n

    left=fibo(n-1)
    right=fibo(n-2)
    return left + right

#print(fibo(9))


def fiboDP(n,memory):
    if n<2:
        return n
    if memory.get(n):
        return memory.get(n)

    left=fiboDP(n-1,memory)
    right=fiboDP(n-2,memory)
    total= left + right
    memory[n]=total
    return total
print(fiboDP(50,{}))