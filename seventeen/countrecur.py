def subsequence(processed,unprocessed,c):
    if len(unprocessed)==0:
        #print(processed)
        c+=1
        return

    ch=unprocessed[0]
    subsequence(processed+ch,unprocessed[1:])
    subsequence(processed,unprocessed[1:])

def count(processed,unprocessed):
    if len(unprocessed)==0:
        if len(processed)==0:
            return 0
        else:
            return 1

    ch=unprocessed[0]
    left=count(processed+ch,unprocessed[1:])
    right=count(processed,unprocessed[1:])
    return left+right

def list_count(processed,unprocessed):
    if len(unprocessed)==0:
        if len(processed)==0:
            return []
        else:
            return [processed]

    ch=unprocessed[0]
    acc=[]
    acc.extend(list_count(processed+ch,unprocessed[1:]))
    acc.extend(list_count(processed,unprocessed[1:]))

    return acc

a=list_count("","abc")
print(a)