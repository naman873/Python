def sub(first,second):
    if (len(first)==0) or (len(second)==0):
        return 0

    if first[0]==second[0]:
        return 1 + sub(first[1:],second[1:])
    else:
        left=sub(first[1:],second)
        right=sub(first,second[1:])
        return max(left,right)

def ret_sub(first,second):
    if (len(first)==0) or (len(second)==0):
        return 0 ,""

    if first[0]==second[0]:
        count,yet=ret_sub(first[1:],second[1:])
        return count+1 , first[0] + yet
    else:
        left_c,left_yet=ret_sub(first[1:],second)
        right_c,right_yet=ret_sub(first,second[1:])

        if left_c > right_c:
            return left_c,left_yet
        else:
            return right_c,right_yet

def ret_li_sub(first,second):
    if (len(first)==0) or (len(second)==0):
        return 0 ,[""]

    if first[0]==second[0]:
        count,yet=ret_li_sub(first[1:],second[1:])
        return count+1 , list(map(lambda item :first[0]+item,yet))
    else:
        left_c,left_yet=ret_li_sub(first[1:],second)
        right_c,right_yet=ret_li_sub(first,second[1:])

        if left_c > right_c:
            return left_c,left_yet
        elif left_c<right_c:
            return right_c,right_yet
        else:
            return left_c,left_yet+right_yet



print(ret_li_sub("manan","aman"))
