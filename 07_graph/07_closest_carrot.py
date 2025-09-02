from collections import deque

def closest_carrot(grid, starting_row, starting_col):
    initial_distance = 0
    
    visited = set( [ (starting_row, starting_col) ] )

    queue = deque([ (starting_row, starting_col, initial_distance) ])


    while queue:
        r, c, d = queue.popleft()

        if grid[r][c] == 'C':
            return d
        
        deltas = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        for delta in deltas:
            delta_row, delta_col = delta
            nbr_row = r + delta_row
            nbr_col = c + delta_col

            row_inbounds = 0 <= nbr_row < len(grid)
            col_inbounds = 0 <= nbr_col < len(grid[0])

            pos = (nbr_row, nbr_col)

            if row_inbounds and col_inbounds and grid[nbr_row][nbr_col] !='X' and pos not in visited:
                queue.append( (nbr_row, nbr_col, d+1) )
                visited.add(pos)

    return -1



grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

print(closest_carrot(grid, 1, 2)) # -> 4
