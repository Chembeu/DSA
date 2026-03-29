def array_print(grid):
    def can_partition(grid):
    m = len(grid)
    n = len(grid[0])
    
    total = sum(sum(row) for row in grid)
    
    # If total is odd → impossible
    if total % 2 != 0:
        return False
    
    target = total // 2
    
    # 🔹 Try horizontal cuts
    current_sum = 0
    for i in range(m - 1):  # ensure bottom is not empty
        current_sum += sum(grid[i])
        if current_sum == target:
            return True
    
    # 🔹 Try vertical cuts
    current_sum = 0
    for j in range(n - 1):  # ensure right is not empty
        col_sum = 0
        for i in range(m):
            col_sum += grid[i][j]
        
        current_sum += col_sum
        
        if current_sum == target:
            return True
    
    return False
