def subseq(processed,unprocessed):
    if len(unprocessed)==0:
        print(processed)
        return
    ch=unprocessed[0]

    subseq(processed +ch,unprocessed[1:])
    subseq(processed,unprocessed[1:])

subseq("","abc")