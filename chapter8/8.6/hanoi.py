def hanoi(n,source,helper,target):
    if n > 0:
        #Move tower of size n-1 to helper
        hanoi(n-1,source,target,helper)
        #Move disk from source to target
        if source:
            target.append(source.pop())
        #move tower of size n-1 from helper to target
        hanoi(n-1,helper,source,target)

source = [4,3,2,1]
target = []
helper = []

hanoi(len(source),source,helper,target)

print(str(source) +str(helper) + str(target))
