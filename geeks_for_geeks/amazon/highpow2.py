import math

def highPow(n):

    for i in range(n,-1,-1):
        if math.log(i,2) % int(math.log(i,2)) == 0:
            return i

def highPowBit(n):
    
    res = 1
    for i in range(0,8):
        res = i
        temp = 1 << i
        if temp > n:
            break
    return 1 << (res - 1)

print(highPowBit(10))
print(highPow(10))
print(highPow(32))
print(highPowBit(32))
