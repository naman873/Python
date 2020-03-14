# def count(processed,unprocessed):
#     if len(unprocessed)==0:
#         return 1
#     acc=0
#     for i in range(len(unprocessed)):
#         c=unprocessed[i]
#         rec=unprocessed[:i]+unprocessed[i+1:]
#         acc+=count(processed+c,rec)
#
#     return  acc

def li_count(processed,unprocessed):
    if len(unprocessed)==0:
        return [processed]
    acc=[]
    for i in range(len(unprocessed)):
        c=unprocessed[i]
        rec=unprocessed[:i]+unprocessed[i+1:]
        acc.extend(li_count(processed+c,rec))

    return  acc

a=li_count("","abc")
print(a)