from grid import Grid
grid = Grid([[1, 2], [3, 4]], sep=", ")
print(grid)  # "1, 2\n3, 4"
grid.append_row([5, 6])
print(grid)  # "1, 2\n3, 4\n5, 6"
grid.pad()
print(grid)
