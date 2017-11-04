def replaceOnRight(table):

    for counter,value in enumerate(table):
        biggest = 0
        for i in range(counter+1,len(table)):
            if biggest < table[i]:
                biggest = table[i]
        table[counter] = biggest
    table[-1] = -1
    return table

def trickReplaceOnRight(table):

    #maximum = table[::-1][0]
    #print(maximum)
    max_from_right = table[-1]
    for i in range(len(table)-1,-1,-1):
        temp = table[i]
        table[i] = max_from_right
        if(max_from_right < temp):
            max_from_right = temp
    table[-1] = -1
    return table

print(replaceOnRight([16,17,4,3,5,2]))
print(trickReplaceOnRight([16,17,4,3,5,2]))
print(replaceOnRight([2,22,16,17,34,3,5,2]))
print(trickReplaceOnRight([2,22,16,17,34,3,5,2]))
