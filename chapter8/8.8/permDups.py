

def permDups(s):
    result = []
    hashmap = buildFreqTable(s)
    _permDups(hashmap,"",len(s),result)
    return result

def buildFreqTable(s):
    hashmap = dict()
    for c in s:
        if c in hashmap:
            hashmap[c] +=1
        else:
            hashmap[c] = 1
    return hashmap

def _permDups(hashmap,prefix,remaining,result):
    if remaining == 0:
        result.append(prefix)
        return
    for c in hashmap.keys():
        count = hashmap[c]
        if count > 0:
            hashmap[c] -= 1
            _permDups(hashmap,prefix + c, remaining -1, result)
            hashmap[c] = count
