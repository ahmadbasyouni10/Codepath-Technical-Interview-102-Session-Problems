# Problem 12: Thistle Hunt
# Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. Write a function `locate_thistles()` that takes in a list of strings `items` and returns a list of the indices of any elements with value `"thistle"`. The indices in the resulting list should be ordered from least to greatest.
# 1. Share 2 questions you would ask to help understand the question:
#   - Should the function be case-sensitive when looking for "thistle"?
#   - What if a word has prefix of thistle or includes thistle

# 2. Write out in plain English what you want to do: 
#   Create an empty list to store the indices
#   Go through each item in the list using enumerate, keeping track of index and value
#   If the item is "thistle", add its index to our list of indices
#   Return the list of indices (array)

# 3. Translate each sub-problem into pseudocode:
#   function locate_thistles(items):
#     indices = empty list
#     for i from 0 to length of items - 1: or enumerate(items)
#       if items[i] is equal to "thistle": or item == "thistle"
#         add i to indices
#     return indices

# 4. Translate the pseudocode into Python and share your final answer:
def locate_thistles(items):
    res = []
    for i, item in enumerate(items):
        if item == "thistle":
            res.append(i)
    return res

# Test the function
items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"] 
print(locate_thistles(items))




# Problem 12: Shuffle
# Write a function shuffle() that accepts a list cards of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]. Return the list in the form [x1,y1,x2,y2,...,xn,yn].
#   - What should the function do if the input list has an odd number of elements?
#   - Should the function modify the original list or return a new one?

# 2. Write out in plain English what you want to do: 
#   For me it helps me visualize this problem by splitting it into 2 arrays, which can be avoided by simply having a result array and then going through the array from index 0 and adding that value then adding the 
#   value at the middle pointer from where the other array starts and simply increase both the i and the middle pointer until the middle is out of bounds. Then, we know we successfully alternated between both halfs
#   of the array and we have our result.

# 3. Translate each sub-problem into pseudocode:
#function shuffle(cards):
#    res = empty list
#    i = length of cards divided by 2 (integer division)
#    arr1 = first half of cards (from start to index i-1)
#    arr2 = second half of cards (from index i to end)
    
#   for i from 0 to length of arr1 - 1:
#      append arr1[i] to res
#        append arr2[i] to res
    
#   return res

# 4. Translate the pseudocode into Python and share your final answer:
def shuffle(cards):
    res = []
    i = len(cards) // 2
    arr1 = cards[:i]
    arr2 = cards[i:]
    for i in range(len(arr1)):
        res.append(arr1[i])
        res.append(arr2[i])
    return res

# Test the function
cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
print(shuffle(cards))




# Problem 8: Local Maximums
# Write a function local_maximums() that accepts an n x n integer matrix grid and returns an integer matrix local_maxes of size (n - 2) x (n - 2) such that: local_maxes[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1. In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid
#   - What if we have less than 3 rows in a 2d array (2x2)
#   - Should the function modify the original list or return a new one?

# 2. Write out in plain English what you want to do: 
# We will brute force it since unavoidable really
# 4 nested loops from top left and one to the right
# then the row below that column 0 and column 1 
# N-2 gives us how many rows and columns count we will have
# the nested for loops within the two nested for loops are going to expand 3 rows and 3 columns to form 3x3 matrix
# we will attempt to update the result using the last nested for loops vars since we want max in the 3x3 matrix

# 3. Translate each sub-problem into pseudocode:
#function local_maximums(grid):
#    N = length of grid
#    res = create a 2D array of size (N-2) x (N-2) filled with zeros
#
#    for i from 0 to N-3:
#        for j from 0 to N-3:
#            for r from i to i+2:
#               for c from j to j+2:
#                    res[i][j] = maximum of (res[i][j], grid[r][c])
    
#    return res

# 4. Translate the pseudocode into Python and share your final answer:
def local_maximums(grid):
        N = len(grid) # 4 
        # 4 - 2 equals how many rows and columns we will have in res (Number of 3x3 we be 0-1 rows 0-1 cols) = 4   3 x 3 
        res = [[0]*(N-2) for _ in range(N-2)]

        for i in range(N-2):
            for j in range(N-2):
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        res[i][j] = max(res[i][j], grid[r][c])
                
        
        return res

# Test the function
grid = [
	[9, 9, 8, 1],
	[5, 6, 2, 6],
	[8, 2, 6, 4],
	[6, 2, 2, 2]
]
print(local_maximums(grid))




# Problem 8: Local Maximums
# Batman has a bomb to defuse, and his time is running out! His butler, Alfred, is on the phone providing him with a circular array code of length n and key k. To decrypt the code, Batman must replace every number. All the numbers are replaced simultaneously. If k > 0, replace the ith number with the sum of the next k numbers. If k < 0, replace the ith number with the sum of the previous k numbers. If k == 0, replace the ith number with 0. As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1]. Given the circular array code and an integer key k, write a function decrypt() that returns the decrypted code to defuse the bomb!
# 

# 2. Write out in plain English what you want to do: 
# We need to have 3 checks if elif and else for each case of k value
# we will use % in python to make sure we dont get out of bounds error, since no out of bounds just go through the array over and over

# 3. Translate each sub-problem into pseudocode:
# Handle k == 0 case
# if k == 0:
#    return [0] * n

#res = [0] * n

#if k > 0:
    # Initialize window sum for positive k
#    window_sum = sum(code[:k])
    
    # Slide window through array
#    for i in range(n):
#        res[i] = window_sum
#        window_sum = window_sum - code[i] + code[(i + k) % n]
#else:
    # Convert negative k to positive
#    k = -k
    
    # Initialize window sum for negative k
#    window_sum = sum(code[-k:])
    
    # Slide window through array
#    for i in range(n):
#        res[i] = window_sum
#        window_sum = window_sum - code[(i - k) % n] + code[i]

# return res

# 4. Translate the pseudocode into Python and share your final answer:
def defuse(code, k):
    res = [0] * len(code)
    for i in range(len(code)):
        if k == 0:
            res[i] = 0
        elif k > 0:
            curSum = 0
            for j in range(1, k+1):
                curSum += code[(i+j) % len(code)]
            res[i] = curSum
        else:
            curSum = 0
            for j in range(1, -k+1):
                curSum += code[i-j]
            res[i] = curSum

    return res

code = [5,7,1,4]
k = 3
print(defuse(code, k))