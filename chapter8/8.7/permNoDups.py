
#Non recursive solution
#Time complexity:
#Memory complexity:
#
def permNoDups(string):
    length = len(string)
    if length == 1:
        return [string]
    i = 0
    permutations = [string]
    last = string[:i] + string[i+1] + string[i] + string[i+2:]
    permutations.append(last)
    i +=1
    while last!= string:
        if i != (length -1):
            last = last[:i] + last[i+1] + last[i] + last[i+2:]
            permutations.append(last)
            i +=1
        else:
            last = last[i] + last[1:i] + last[0]
            permutations.append(last)
            i = 0
    new = []
    for i in range(1,len(permutations[:-1]),2):
        new.append(permutations[i][-1] + permutations[i][1:-1] + permutations[i][0])
        new.append(permutations[i+1][-1] + permutations[i+1][1:-1] + permutations[i+1][0])
   # for i in range(0,len(permutations[:-1]),3):
    #    new.append(permutations[i][] + permutations[i][])
    return new + permutations[:-1]

def permNoDupsRec(string):
    if len(string) != 1:
        prev_results = permNoDupsRec(string[:-1])
        res = []
        last = string[-1]
        for i in prev_results:
            for j in range(len(i)+1):
                if j == 0:
                    new_string = last + i
                elif j == len(i):
                    new_string = i + last
                else:
                    new_string = i[:j] + last + i[j:]
                res.append(new_string)
        return list(set(res))
    else:
        return [string]

tut = permNoDups("abcd")
tot = permNoDupsRec("abcd")
print(str(tut))
print(str(tot))
for i in tot:
    if i not in tut:
        print(i)
