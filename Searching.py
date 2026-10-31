

def binary_search(nums, target):
    first_idx, last_idx = -1, -1
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            first_idx = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
                
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            last_idx = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return [first_idx, last_idx]

def binary_search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    m = len(matrix)
    n = len(matrix[0])
    
    left = 0
    right = (m * n) - 1
    
    while left <= right:
        mid = (left + right) // 2
        row = mid // n
        col = mid % n
        
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return False