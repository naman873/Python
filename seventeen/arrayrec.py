def is_sorted(li,index=0):
    if index==(len(li)-1):
        return True

    current=li[index]<=li[index+1]

    remaining=is_sorted(li,index+1)

    return current and remaining

def contain(li,target,index=0):
    if index==len(li):
        return False

    current=li[index]==target

    remaining=contain(li,target,index+1)
    return current or remaining


print(contain([11,2,44],44))
