

def getBit(number,index):
    return (number & (1<< index) !=0 )

def flipBit(number,index):
    return( number | (1 <<index))

def nextNumber(anumber):
    #Flip last bit that is 1
    ones_counter = []
    for i in range(0,8):
        res = getBit(anumber,i)
        if res:
            ones_counter.append(i)
    #Get next largest:
    number_of_ones = len(ones_counter)
    if len(ones_counter) != 7:
        mask = ""   
        for i in range(number_of_ones):
            mask += "1"
        nextBig = int(mask,2) << (7 - number_of_ones)
        #Get nex smallest
        mask = ""
        #Get index of smallest one:
        smallest = 0
        for i in range(number_of_ones):
            if i >= smallest:
                smallest = i
        #Set smallest to 0
        flipBit(anumber,smallest)
        #Check if next is free:
        while True:
            smallest -= 1
            if getBit(anumber,smallest) == False:
                flipbit(anumber,smallest)
                return nextBig,anumber
                
    else:
        print("No next number!")
        return None


