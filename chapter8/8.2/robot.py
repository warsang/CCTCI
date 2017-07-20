
def find_path(grid):
    if grid is None or len(grid) == 0:
        return None
    path = list()
    if _find_path(grid, len (grid)-1,len(grid[0])-1,path):
        return path
    return None

def _find_path(grid,r ,c, path):
    if r < 0 or c < 0 or not grid[r][c]:
        return False
    if ((r == 0) and (c == 0)) or _find_path(grid,r-1,c,path) or _find_path(grid,r,c-1,path):
        path.append((r,c))
        return True
    return False


def find_path_optimised(grid):
    if grid is None or len(grid) == 0:
        return None
    path = list()
    cache = dict()
    if _find_path_optimised(grid, len (grid)-1,len(grid[0])-1,path,cache):
        return path
    return None


def _find_path_optimised(grid,r,c,path,cache):
    if r < 0 or c < 0 or not grid[r][c]:
        return False
    try:
        return cache[(r,c)]
    except:
        in_path = False
        if ((r == 0) and (c == 0)) or _find_path(grid,r-1,c,path) or _find_path(grid,r,c-1,path):
            path.append((r,c))
            in_path = True
        cache[(r,c)] = in_path
        return in_path

def main():
    r = 15
    c = 15
    grid = [[None]*(r+1)]*(c+1)
    print(find_path(grid))
    print(find_path_optimised(grid)) 

if __name__=="__main__":
    main()


