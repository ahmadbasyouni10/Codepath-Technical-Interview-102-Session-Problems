# Problem 7: Post Compare
# You often draft your posts and edit them before publishing. Given two draft strings draft1 and draft2,
# return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will remain empty.

# 1. Share 2 questions you would ask to help understand the question:
#   - What should happen if there are multiple backspaces in a row?
#   - Does '#' only apply to the immediate previous character, or could it backtrack further?

# 2. Write out in plain English what you want to do:
#   Use a helper function to simulate typing for both strings, managing backspace characters correctly.
#   Compare the final results of the two typed strings.

# 3. Translate each sub-problem into pseudocode:
#   - Define a helper function to process backspaces:
#       - Loop through each character of the input string.
#       - If the character is '#', pop from the stack if it's not empty.
#       - Otherwise, add the character to the stack.
#   - Use the helper function to process both draft1 and draft2.
#   - Return True if both processed versions are the same.

# 4. Translate the pseudocode into Python and share your final answer:
def helper(word, stack):
    for c in word:
        if c == "#":
            if stack:
                stack.pop()
        else:
            stack.append(c)

def post_compare(draft1, draft2):
    stack1 = []
    stack2 = []
    helper(draft1, stack1)
    helper(draft2, stack2)
    return stack1 == stack2

print(post_compare("ab#c", "ad#c"))  # True
print(post_compare("ab##", "c#d#"))  # True
print(post_compare("a#c", "b"))      # False

# Problem: Make Smallest Watchlist
# Given a string "watchlist," convert it into the smallest lexicographical palindrome possible by replacing the characters.

# 1. Share 2 questions you would ask to help understand the question:
#   - Can we replace any character with any other character, or do we need to use characters from the original string?
#   - Should the resulting palindrome be lexicographically smallest, or just any valid palindrome?

# 2. Write out in plain English what you want to do:
#   Convert the given string into a palindrome by modifying the characters from both ends, making sure that the final palindrome is the smallest possible lexicographically.

# 3. Translate each sub-problem into pseudocode:
#   - Convert the input string into a list to allow modification.
#   - Set two pointers, "l" (left) starting from the beginning, and "r" (right) starting from the end of the list.
#   - Traverse from both ends towards the center:
#       - If the characters at "l" and "r" are different:
#           - Replace the greater character with the smaller one to ensure lexicographical order.
#       - Move both pointers towards the center.
#   - Return the modified list joined back into a string.

# 4. Translate the pseudocode into Python and share your final answer:
def make_smallest_watchlist(watchlist):
    # Convert the string to a list for mutability
    watchlist = list(watchlist)
    # Set pointers to the beginning and end
    l = 0
    r = len(watchlist) - 1

    # Traverse the string until the pointers meet
    while l < r:
        # If the characters are different
        if watchlist[l] != watchlist[r]:
            # Replace the greater character with the smaller one
            if ord(watchlist[l]) < ord(watchlist[r]):
                watchlist[r] = watchlist[l]
            else:
                watchlist[l] = watchlist[r]
        # Move pointers towards the center
        l += 1
        r -= 1

    # Join the list back into a string and return it
    return ''.join(watchlist)

# Test cases
print(make_smallest_watchlist("egcfe"))  # Output: "efcfe"
print(make_smallest_watchlist("abcd"))   # Output: "abba"
print(make_smallest_watchlist("seven"))  # Output: "seves"

# Problem: Mark Event Timeline
# Given an event string and a timeline string, determine the indices where you need to place the event in the timeline such that the resulting timeline matches exactly.

# 1. Share 2 questions you would ask to help understand the question:
#   - Can events overlap when placing them in the timeline?
#   - Is there a maximum number of placements we should attempt before concluding it's not possible?

# 2. Write out in plain English what you want to do:
#   Use a breadth-first search (BFS) to try placing the event at different positions in the timeline.
#   Track the positions where events are placed until we either match the entire timeline or exhaust our possibilities.
#   Return the list of indices where the event was placed.

# 3. Translate each sub-problem into pseudocode:
#   - Create a queue to perform BFS, starting with an empty timeline and no indices recorded.
#   - Define helper functions to check if the event can be placed at a given start position and to place the event.
#   - Iterate through possible starting positions:
#       - If the event can be placed, create a new version of the timeline with the event inserted and add it to the queue.
#       - If the modified timeline matches the original, return the list of indices.
#   - If no valid solution is found within a set number of iterations, return an empty list.

# 4. Translate the pseudocode into Python and share your final answer:
from collections import deque

def mark_event_timeline(event, timeline):
    t_len = len(timeline)
    event_len = len(event)
    # Initialize the queue with an empty timeline and an empty list of indices
    queue = deque([(['?'] * t_len, [])])
    max_turns = 10 * t_len

    # Helper function to check if the event can be placed
    def can_place(t, event, start):
        for i in range(event_len):
            if t[start + i] != '?' and t[start + i] != event[i]:
                return False
        return True

    # Helper function to place the event in the timeline
    def place_event(t, event, start):
        new_t = t[:]
        for i in range(event_len):
            new_t[start + i] = event[i]
        return new_t

    # Use BFS to try placing the event
    turns = 0
    while queue and turns < max_turns:
        current_t, indices = queue.popleft()
        # Iterate over possible start positions
        for i in range(t_len - event_len + 1):
            if can_place(current_t, event, i):
                # Create a new timeline with the event placed
                new_t = place_event(current_t, event, i)
                new_indices = indices + [i]
                # If the modified timeline matches the target, return the indices
                if ''.join(new_t) == timeline:
                    return new_indices
                # Add the new timeline and indices to the queue
                queue.append((new_t, new_indices))
        turns += 1

    # Return an empty list if no solution is found
    return []

# Example usage
print(mark_event_timeline("abc", "ababc"))     # Output: [0, 2]
print(mark_event_timeline("abca", "aabcaca"))  # Output: [3, 0, 1]

# Problem: Validate Shelter Sequence
# Given two lists, `admitted` and `adopted`, determine if the sequence of adopted animals is possible given the order of admitted animals. 
# The shelter follows a "last in, first out" system, similar to a stack.

# 1. Share 2 questions you would ask to help understand the question:
#   - Can an animal be adopted immediately after admission, or must it wait until others have been admitted?
#   - Will the `admitted` and `adopted` lists always contain the same animals, and will all animals be adopted?

# 2. Write out in plain English what you want to do:
#   Use a stack to simulate the admission and adoption of animals. Push animals onto the stack as they are admitted. 
#   Whenever the animal at the top of the stack matches the next one to be adopted, pop it from the stack.
#   At the end, if the stack is empty, then the sequence of adoptions was valid.

# 3. Translate each sub-problem into pseudocode:
#   - Initialize an empty stack and a pointer `i` for the `adopted` list.
#   - Loop through each animal in `admitted`:
#       - Push the animal onto the stack.
#       - While the stack is not empty and the top of the stack matches the current `adopted` animal:
#           - Pop the top animal from the stack and move the pointer to the next adopted animal.
#   - If the stack is empty at the end, return True, else return False.

# 4. Translate the pseudocode into Python and share your final answer:
def validate_shelter_sequence(admitted, adopted):
    i = 0
    stack = []
    # Loop through each animal in admitted
    for a in admitted:
        stack.append(a)
        # While the stack is not empty and the top matches the next adopted animal
        while stack and stack[-1] == adopted[i]:
            stack.pop()
            i += 1
    # Return True if the stack is empty (all animals were adopted in valid order)
    return True if not stack else False

# Example usage
print(validate_shelter_sequence([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))  # Output: True
print(validate_shelter_sequence([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))  # Output: False

# Problem: Sort Performances by Type
# Given an array of integers, sort them into two types: even and odd. 
# The output should contain all even numbers first, followed by all odd numbers.

# 1. Share 2 questions you would ask to help understand the question:
#   - Should the order of the even and odd numbers be maintained from the original array?
#   - What should happen if the input array is empty or contains only one type of number (all even or all odd)?

# 2. Write out in plain English what you want to do:
#   Use two stacks to separate the numbers into even and odd. 
#   Iterate through the input array and push each number onto the appropriate stack based on its type. 
#   Finally, concatenate the even stack with the odd stack and return the result.

# 3. Translate each sub-problem into pseudocode:
#   - Initialize two empty stacks: stack1 for even numbers and stack2 for odd numbers.
#   - Loop through each number in the input array:
#       - If the number is even, append it to stack1.
#       - If the number is odd, append it to stack2.
#   - Return the concatenation of stack1 and stack2.

# 4. Translate the pseudocode into Python and share your final answer:
def sort_performances_by_type(arr):
    stack1 = []  # Stack for even numbers
    stack2 = []  # Stack for odd numbers
    # Loop through each number in the input array
    for num in arr:
        if num % 2 == 0:
            stack1.append(num)  # Add to stack1 if even
        else:
            stack2.append(num)  # Add to stack2 if odd
    # Concatenate the two stacks and return
    return stack1 + stack2

# Example usage
print(sort_performances_by_type([1, 2, 3, 4, 5]))   # Output: [2, 4, 1, 3, 5]
print(sort_performances_by_type([10, 15, 20, 25, 30]))  # Output: [10, 20, 30, 15, 25]


# Problem: Check for Prefix of Signal
# Given a sentence and a prefix string, determine if any word in the sentence starts with the given prefix.
# Return the index (1-based) of the first word that matches, or -1 if no such word exists.

# 1. Share 2 questions you would ask to help understand the question:
#   - Should the comparison be case-sensitive or case-insensitive?
#   - What should happen if the prefix is an empty string or if the sentence contains only spaces?

# 2. Write out in plain English what you want to do:
#   Split the sentence into words and iterate through each word.
#   For each word, check if it starts with the given prefix by comparing characters. 
#   If a match is found, return the 1-based index of that word. If no matches are found, return -1.

# 3. Translate each sub-problem into pseudocode:
#   - Split the sentence into a list of words.
#   - Loop through each word in the list:
#       - Initialize a variable j to track the index of the prefix.
#       - Loop through each character of the current word:
#           - If the current character matches the character in the prefix at index j, increment j.
#           - If j reaches the length of the prefix, return the index of the word (1-based).
#   - If no word matches the prefix, return -1.

# 4. Translate the pseudocode into Python and share your final answer:
def is_prefix_of_signal(sentence, pre):
    words = sentence.split(" ")  # Split the sentence into words
    for z in range(len(words)):   # Loop through each word
        word = words[z]            # Get the current word
        j = 0                       # Initialize prefix index
        for i in range(len(word)):  # Loop through each character of the word
            if word[i] == pre[j]:    # If character matches prefix
                j += 1               # Increment prefix index
                if j == len(pre):     # Check if prefix is fully matched
                    return z + 1      # Return the 1-based index of the word
            if j == len(pre):        # If prefix matched completely
                return z + 1
    return -1                        # Return -1 if no match found

# Example usage
print(is_prefix_of_signal("i love eating burger", "burg"))  # Output: 4
print(is_prefix_of_signal("this problem is an easy problem", "pro"))  # Output: 2
print(is_prefix_of_signal("i am tired", "you"))  # Output: -1


# Problem: Next Greater Dream
# Given a list of dreams represented as integers, return a list where each element at index i is replaced by the next greater dream.
# If there is no next greater dream for an element, it is replaced by -1. The dreams list is considered circular.

# 1. Share 2 questions you would ask to help understand the question:
#   - Should the function consider elements in the list that are the same when determining the "next greater" value?
#   - What should be the output if the input list is empty or has only one element?

# 2. Write out in plain English what you want to do:
#   Use a stack to keep track of the indices of dreams while iterating through the list. 
#   For each dream, check if it is greater than the dreams at the indices stored in the stack. 
#   If it is, pop those indices from the stack and set the corresponding results to the current dream value.
#   Since the list is circular, iterate through the list twice.

# 3. Translate each sub-problem into pseudocode:
#   - Initialize a stack to keep track of indices and a results list with -1.
#   - Loop through the dreams list twice (to account for the circular nature):
#       - While the stack is not empty and the current dream is greater than the dream at the index at the top of the stack:
#           - Pop from the stack and set the result for that index to the current dream.
#       - If in the first loop (i < n), push the current index onto the stack.
#   - Return the results list.

# 4. Translate the pseudocode into Python and share your final answer:
def next_greater_dream(dreams):
    stack = []                   # Stack to keep track of indices
    n = len(dreams)              # Length of dreams list
    res = [-1] * n               # Result list initialized to -1
    for i in range(n * 2):       # Loop through the dreams list twice
        while stack and dreams[stack[-1]] < dreams[i % n]:
            res[stack.pop()] = dreams[i % n]  # Update result for the popped index
        if i < n:                # Only push indices from the first loop
            stack.append(i)
    return res                   # Return the final results

# Example usage
print(next_greater_dream([1, 2, 1]))          # Output: [2, -1, 2]
print(next_greater_dream([1, 2, 3, 4, 3]))    # Output: [2, 3, 4, -1, 4] 

# Problem: Token Value
# Given a string token consisting of '(' and ')', return the value of the token, 
# which is the number of pairs of parentheses that are correctly matched.
# If there are unmatched closing parentheses, return -1.

# 1. Share 2 questions you would ask to help understand the question:
#   - How should the function handle strings that consist only of closing parentheses?
#   - Should the function consider nested parentheses as additional values, or just count the pairs?

# 2. Write out in plain English what you want to do:
#   Use a stack to keep track of opening parentheses. 
#   For each closing parenthesis encountered, check if there is a corresponding opening parenthesis on the stack.
#   If there is, pop from the stack and increment the value. If there is no matching opening parenthesis, return -1.
#   After processing the string, return the total value of matched pairs.

# 3. Translate each sub-problem into pseudocode:
#   - Initialize a variable val to keep count of matched pairs and a stack to track opening parentheses.
#   - Loop through each character in the token:
#       - If the character is ')':
#           - Check if the stack is not empty:
#               - Pop from the stack and increment val.
#           - Otherwise, return -1 (unmatched closing parenthesis).
#       - If the character is '(', append it to the stack.
#   - Return val after processing all characters.

# 4. Translate the pseudocode into Python and share your final answer:
def token_value(token):
    val = 0                       # Initialize value to count matched pairs
    stack = []                    # Stack to keep track of opening parentheses
    for c in token:               # Loop through each character in the token
        if c == ")":              # Check for closing parenthesis
            if stack:             # If stack is not empty
                stack.pop()       # Pop from stack (matching opening parenthesis)
                val += 1          # Increment the count of matched pairs
            else:
                return -1         # Return -1 for unmatched closing parenthesis
        else:
            stack.append(c)       # Append opening parenthesis to stack
    return val                    # Return the total count of matched pairs

# Example usage
print(token_value("()"))         # Output: 1
print(token_value("(())"))       # Output: 2
print(token_value("()()"))       # Output: 2