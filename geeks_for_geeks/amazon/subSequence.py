def countSubseq(string):

    aCount = bCount = cCount = 0

    for i in string:
        if i == 'a':
            aCount = 1 + 2 * aCount
        elif i == 'b':
            bCount = aCount + 2 * bCount
        elif i =='c':
            cCount = bCount + 2 * cCount
        else:
            return 0
    return cCount

print(countSubseq('abcabc'))
