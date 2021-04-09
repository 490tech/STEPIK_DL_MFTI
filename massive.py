def cumsum_and_erase (A, erase=1):
    B=[]
    C=0

    for i in range (len(A)):
        C=C+A[i]
        if C==erase:
            continue
        else:
            #print (C)
            B.append (C)
    return B