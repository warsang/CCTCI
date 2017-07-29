def getBit(number,index):
    return (number & (1 << index) != 0)

def setBit(number,index):
    return (number | (1 << index))

def clearBit(number,index):
    return (number & (~(1 << index)))

def updateBit(number,index,value):
    if value != 0 or value !=1:
        raise 'error'
    else:
        #ClearBit
        mask = ~(1 << index)
        number = number & mask
        #Set bit to value
        return number | (value << index)


