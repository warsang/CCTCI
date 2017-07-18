
#full_ones = 4294967296
full_ones = int('11111111111',2)

def bitInsert(N,M,i,j):

    a = (1 << i) -1
    a = a ^ full_ones
    b=(1 << j) -1
    b = b ^ full_ones
    mask = a + b
    N = N & mask
    M = M << i
    result = M +N
    return result

one = int('10000000000', 2)
two = int('10011', 2)
res = bitInsert(one,two,2,6)
print(bin(res))

