hashtable = {0:0, 1:1, 2:2}

def countBits(n):
    
    if n not in hashtable:
        counter = 0
        bitString = (bin(n)[2:])
        for i in bitString:
            if i == '1':
                counter += 1
        hashtable[n] = counter + countBits(n-1)
    
    return hashtable[n]

print(countBits(6))
print(countBits(18))
