import copy

#Time complexity: O(b) with b length of sequence
#O(b) memory
def findZeros(bit_string):
    zeros = []
    for i in range(0,len(bit_string)):
        if bit_string[i] == '0':
            zeros.append(i)
    return zeros

def countOnes(the_string):
    counter = 0
    longest = 0
    for char in the_string:
        if char == '1':
            counter += 1
        else:
            if counter > longest:
                longest = counter
            counter = 0
    if counter > longest:
        longest = counter
    return longest

def flip2Win(number):
    bit_string = bin(number)[2:]
    bit_array = []
    zeros = findZeros(bit_string)
    for element in bit_string:
        bit_array.append(element)
    possibles = []
    for index in zeros:
        temp = copy.copy(bit_array)
        temp[index] = '1'
        possibles.append(countOnes(temp))
    return max(possibles)

def main():
    num = 1775
    print(flip2Win(num))

if __name__ == "__main__":
    main()



