import re

def simplify(poly):
    #First decompose
    dec1 = re.findall(r"[a-z]+", poly)
    for index,a in enumerate(dec1):
        dec1[index] = ''.join(sorted(a))
    #Second decompose
    dec2 = re.findall(r"[\-|\+][2-9]+|[\-|\+]|[2-9]+",poly)
    newpoly = ''
    if len(dec2)!= len(dec1):
        newpoly += dec1[0]
        for i in range(1,len(dec1)):
            newpoly += dec2[i-1] + dec1[i]
    else:
        for i in range(0,len(dec1)):
            newpoly += dec2[i] + dec1[i]
    poly = newpoly
    #Second sort
    temp = re.findall(r"[\-|\+][\w]+|[\w]+", poly)
    temp.sort()
    temp2 = re.findall(r"[a-z]+",poly)
    temp2.sort()
    temp2 = list(set(temp2))
    hash_table = dict()
    result = []
    for element in temp2:
        length = len(element)
        hash_table[element] = [[],[]]
        for i in temp:
            letters = re.findall(r"[a-z]+",i)
            if letters[0] == element:
                coeff_l = re.findall(r"[0-9]+",i)
                if len(coeff_l) != 0:
                    for j in coeff_l:
                        coeff = int(j)
                else:
                    coeff = 0
                if i[0] == '-':
                    if coeff != 0:
                        for j in range(coeff):
                            hash_table[element][0].append(element)
                    else:
                        hash_table[element][0].append(element)
                elif i[0] == '+':
                    if coeff != 0:
                        for j in range(coeff):
                            hash_table[element][1].append(element)
                    else:
                        hash_table[element][1].append(element)
                else:
                    if coeff != 0:
                        for j in range(coeff):
                            hash_table[element][1].append(element)
                    else:
                        hash_table[element][1].append(element)
    for element in temp2:
        difference =len(hash_table[element][1]) - len(hash_table[element][0])
        if difference > 0:
            if difference == 1:
                hash_table[element] = '+'
            else:
                hash_table[element] = '+' + str(difference)
        elif difference < 0:
            if difference == -1:
                hash_table[element] =  '-'
            else:
                hash_table[element] = str(difference)
        else:
            hash_table[element] = ''
    temp3 = []
    for index,element in enumerate(temp2):
        if hash_table[element] == '':
            continue
        temp3.append(hash_table[element] + element)
    #Monomial reordering
    print(temp3)
    merge_sort(temp3)
    print(temp3)
    #lexicographic reordering

    return_string = ''.join(temp3)
    if return_string[0] == '+':
        return_string = return_string[1:]
    print(return_string)

def merge_sort(array):
    if len(array) > 1:
        mid = len(array)//2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if len(re.findall(r"[a-z]+",lefthalf[i])[0]) < len(re.findall(r"[a-z]+",righthalf[j])[0]):
                array[k] = lefthalf[i]
                i = i+1
            else:
                array[k] = righthalf[j]
                j = j+1
            k = k+1
        while j < len(righthalf):
            array[k] = righthalf[j]
            j = j + 1
            k = k +1
        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i = i+1
            k = k+1
        return
simplify("-a+5ab+3a-c-2a")
simplify("a+ac-ab")
#simplify("dc+cdba")
#simplify('2xy-yx')
simplify('-abc+3a+2ac')
simplify('xzy+zby')
