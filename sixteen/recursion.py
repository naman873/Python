# def power(x,p):
#     if p==0:
#         return 1
#     proc=power(x,p-1)
#     return x*proc
# print(power(2,10))




###  finbonaci

def fibo(n):
    if n<2:
        return n

    first=fibo(n-1)
    second=fibo(n-2)
    return  first + second

fibo(5)


