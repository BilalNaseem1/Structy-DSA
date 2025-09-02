def explore(grid, r, c, visited):
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])

    if not row_inbounds or not col_inbounds:
        return False
    
    if grid[r][c] == 'W':
        return False
    
    pos = (r, c)

    if pos in visited:
        return False
    
    explore(grid, r-1, c, visited)
    explore(grid, r+1, c, visited)
    explore(grid, r, c+1, visited)
    explore(grid, r, c-1, visited)

    return True


def island_count(grid):
    visited = set()
    count = 0

    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            if explore(grid, r, c, visited) == True:
                count +=1

    return count