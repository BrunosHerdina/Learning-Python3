def gridChallenge(grid):
    for i in range(len(grid)):
        grid[i]="".join(sorted(list(grid[i])))
    for i in range(len(grid)-1):
        for c in range(len(grid[0])):
            if grid[i+1][c]<grid[i][c]:
                return("NO")
    return("YES")
