

def isMeta(first,second):

    if len(first) != len(second):
        return False
    #Create hashtable and map occurence of each letter
    first_dict = dict()
    second_dict = dict()
    if first == second:
        return False
    for char in first:
        try:
            first_dict[char] += 1
        except:
            first_dict[char] = 1
    for char in second:
        try:
            second_dict[char] += 1
        except:
            second_dict[char] = 1
    for key in first_dict:
        if first_dict[key] != second_dict[key]:
            return False

        #Do a permutation to check if equal:
    for i in range(len(second)):
        for j in range(i+1,len(second)):
            helper = second
            helper = switch(helper,i,j)
            if helper == first:
                return True
    return False

#Switch to values in an array
def switch(array,i,j):
    #Strings are immutable hence a small work around: Other solution would have been to creat a list of chars to represent each string
    new = ''
    for k in range(i):
        new += array[k]
    new += array[j]
    for k in range(i+1, j):
        new += array[k]
    new += array[i]
    for k in range(j+1, len(array)):
        new += array[k]
    return new

def format_input(testCases,array):
    for i in range(0,len(array),2):
        print(isMeta(array[i],array[i+1]))

tested = ['geeks','keegs','geeks','geeks']

format_input(2,tested)
