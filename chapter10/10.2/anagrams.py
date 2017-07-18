#import IPython
#Easy solution: (most pythonic)
def group_anagrams(string_array):
    return sorted(string_array,key=lambda m: sorted(m))

#Harder solution (Not as pythonic but show more thinking)

def group_anagrams_hard(string_array):
    #First we need to sort each word of the array so that anagrams have the same 'print'
    #and can be sorted one next to the other
    helper = []
    final = []
    for word in string_array:
       helper.append(radix_sort(word))
    #We can map all letters to an int value
    #Thankfully python has an already built in metho to do so: ord()
    #ord converts a unicode character back to the integer associated to this value

     #Now we can move all anagrams one close to the other:
    final = [None] * len(string_array)
    counter = 0
    for i,word_one in enumerate(helper):
        match = False
        for j in range(i+1,len(helper)):
            if word_one == helper[j] and i != j :
                match =True
                #Move:
                if final[i] is None:
                    final[counter] = string_array[i]
                else:
                    final.insert(counter,string_array[i])
                final.insert(counter + 1, string_array[j])
                counter += 2
        if not match:
            final.append(string_array[i])
    return final

#Radix sort is 0(kn) with k the number of passes. This seems better than quick sort which is 0(nlog(n)) as we are working with small words (chars only from the english language)
def radix_sort(word):
    helper=[]
    num_word = []
    for char in word:
        num_word.append(ord(char))
    radixsort(num_word)
    word = []
    for element in num_word:
        element = chr(element)
        word.append(element)
    return "".join(word)


def radixsort(aList):
    RADIX = 10
    maxLength = False
    tmp, placement = -1, 1

    while not maxLength:
        maxLength = True
        # declare and initialize buckets
        buckets = [list() for _ in range(RADIX)]

        # split aList between lists
        for i in aList:
            tmp = i / placement
            buckets[tmp % RADIX].append(i)
            if maxLength and tmp > 0:
                maxLength = False

        # empty lists into aList array
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                aList[a] = i
                a += 1

        # move to next digit
        placement *= RADIX

test = ['aloa', 'babybel', 'belbaby', 'ejdov', 'loaa', 'monoko', 'osdcjldv', 'vodej']

print(group_anagrams(test))
print(group_anagrams_hard(test))
