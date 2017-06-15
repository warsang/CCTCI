import unittest


def pal_perm(string):
    
    toto = dict()

    for c in string :
        try: 
            toto[ord(c)] += 1
        except:
            toto[ord(c)] = 1

    boolean = False
    for key,value in toto.items():
        if value %2 != 0:
            if value == 1:
                if boolean:
                    return False
                else:
                    boolean = True
            else:
                return False
    return True


    
string1 = "socatoa"
string2 = "totoabobo"


print(pal_perm(string1))
print(pal_perm(string2))

