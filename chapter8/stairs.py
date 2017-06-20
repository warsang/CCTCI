


def _count_stair_paths(n,memo):
   
    if n < 0:
        return 0
    if n == 0:
        return 1
    if memo[n] is None:
        memo[n] =  _count_stair_paths(n-3,memo) +  _count_stair_paths(n-2,memo) +  _count_stair_paths(n-1,memo)
    return memo[n]

def count_stair_paths(n):

    memory = [None] * (n + 1)
    return _count_stair_paths(n,memory)

print(count_stair_paths(100))
