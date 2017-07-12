import unittest

def oneAway(string1,string2):
    length1 = len(string1)
    length2 = len(string2)
    if length1 != length2 and length1 != (length2 + 1) and length1 != (length2 -1):
        return False
    differences = 0
    #Case1: replace
    if length1 == length2:
        #Itterate first and second string and check if only one different letter
        for i in range(0,length1):
            if string1[i] != string2[i]:
                differences +=1
    #Case2: Insert in 2
    elif length1 == (length2 + 1):
        differences = insert(string1,string2)
    #Case3: Insert in 1
    else:
        differences = insert(string2,string1)
    if differences > 1:
        return False
    else: 
        return True


def insert(string1,string2):
    i = 0
    j = 0
    insert_counter = 0
    while i <= (len(string1) - 1) or j <= (len(string2) - 1):
        if j == len(string2) :
            insert_counter += 1
            break
        if string1[i] == string2[j]:
            i += 1
            j += 1
        else:
            insert_counter += 1
            i += 1
    return insert_counter

class Test(unittest.TestCase):

    def test_stuff(self):
        self.assertTrue(oneAway('pale','ple'))
        self.assertTrue(oneAway('pales','pale'))
        self.assertTrue(oneAway('pale','bale'))
        self.assertFalse(oneAway('pale','bake'))

if __name__ == "__main__" :
    unittest.main()
