def perm(processed,unporcessed):
    if len(unporcessed) == 0:
        print(processed)
        return

    for i in range(len(unporcessed)):
        ch=unporcessed[i]
        chunk=unporcessed[:i]+unporcessed[i+1:]
        perm(processed+ch,chunk)



perm("" ,"abc")