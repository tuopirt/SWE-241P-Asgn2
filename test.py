from Searching import binary_search, binary_search_matrix

# Task 1: Find First and Last Position of Element in Sorted Array
# Task 1 Simple Test
assert binary_search([4, 9, 10, 13, 17, 17, 19, 21], 17) == [4, 5]
assert binary_search([1, 2, 3], 2) == [1, 1]
print("Task 1 Simple Test Passed")

# Task 1 Medium Test
assert binary_search([5, 7, 7, 8, 8, 10], 8) == [3, 4]
assert binary_search([2, 2, 2, 2, 2], 2) == [0, 4]
print("Task 1 Medium Test Passed")

# Task 1 Hard Test (Edge cases & missing/empty checks)
assert binary_search([], 0) == [-1, -1]
assert binary_search([1], 1) == [0, 0]
assert binary_search([1], 2) == [-1, -1]
assert binary_search([2, 4, 6, 8, 10, 14, 16], 12) == [-1, -1]
print("Task 1 Hard Test Passed")


# Task 2: Search a 2D Matrix
# Task 2 Simple Test
matrix_sample = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
assert binary_search_matrix(matrix_sample, 3) == True
assert binary_search_matrix(matrix_sample, 13) == False
print("Task 2 Simple Test Passed")

# Task 2 Medium Test
matrix_small = [[1]]
assert binary_search_matrix(matrix_small, 1) == True
assert binary_search_matrix(matrix_small, 0) == False

matrix_medium = [
    [1, 3, 5],
    [7, 9, 11]
]
assert binary_search_matrix(matrix_medium, 5) == True
assert binary_search_matrix(matrix_medium, 6) == False
print("Task 2 Medium Test Passed")

# Task 2 Hard Test (Edge cases: empty matrix, boundaries)
assert binary_search_matrix([], 5) == False
assert binary_search_matrix([[]], 5) == False
assert binary_search_matrix(matrix_sample, 1) == True
assert binary_search_matrix(matrix_sample, 60) == True
print("Task 2 Hard Test Passed")