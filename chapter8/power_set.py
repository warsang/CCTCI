cache = []

def recursive_func(the_set, the_subset):

    if len(the_set) == 1:
        return the_subset
    for element in the_subset:
        try:
            the_set.remove(element)
        except:
            pass

    for element in the_set.copy():
        temp = the_subset
        temp.append(element)
        cache.append(temp)
        recursive_func(the_set,temp)



def power_set(the_set):
    for element in the_set.copy():
        recursive_func(the_set,[element])


def getSubsets(the_set,index):
    allsubsets = []

    if(len(the_set) == index):
        allsubsets.append([])
    else:
        allsubsets = getSubsets(the_set, index + 1)
        item = the_set[index]
        moresubsets = []
        for subset in allsubsets:
            newsubset = subset
            newsubset.append(item)
            moresubsets.append(newsubset)
        allsubsets += moresubsets
    return allsubsets

a_set = [1,2,3]
power_set(a_set)
print(cache)
print(getSubsets(a_set,0))
