# Problem 1: Count Critical Points in a Linked List

# Understand:
# - We need to count the "critical points" in a linked list.
# - A critical point is a node whose value is strictly larger or smaller than its immediate neighbors.

# Match:
# - We can solve this by traversing the list node by node.
# - For each node, we compare it with the previous and next nodes to check if it forms a peak or valley.

# Plan:
# 1. Create a Node class to represent each element in the linked list.
# 2. Implement a function `count_critical_points`:
#    - Traverse the list using three pointers: `prev`, `cur`, and `nxt`.
#    - If `cur` is a peak or valley, increment the counter.
# 3. Test with an example list: 5 -> 3 -> 1 -> 2 -> 5 -> 1 -> 2

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def count_critical_points(song_audio):
    # Initialize counter for critical points
    res = 0  
    prev = song_audio  # Previous node
    cur = prev.next  # Current node

    # Traverse the list while checking for critical points
    while cur and cur.next:
        nxt = cur.next  # Next node
        # Check if 'cur' is a peak or valley
        if (cur.value < prev.value and cur.value < nxt.value) or (cur.value > prev.value and cur.value > nxt.value):
            res += 1  # Increment critical points counter
        # Move the pointers to the next set of nodes
        prev = cur
        cur = nxt

    return res

# Test the function
song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2))))))
print(count_critical_points(song_audio))  # Output: 3

# ---------------------------------------------------

# Problem 2: Find the Start of a Loop in a Linked List

# Understand:
# - We need to detect if there is a cycle (loop) in a linked list.
# - If a cycle exists, we need to return the starting point of the loop.

# Match:
# - We can use Floyd's Tortoise and Hare algorithm to detect cycles.
# - If a cycle is detected, reset one pointer to the head and move both pointers until they meet at the loop start.

# Plan:
# 1. Create a Node class to represent each element in the linked list.
# 2. Implement a `loop_start` function:
#    - Use two pointers (slow and fast) to detect the cycle.
#    - Reset one pointer to the head and move both pointers at the same speed to find the loop start.
# 3. Test with an example linked list with a loop.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def loop_start(path_start):
    slow = path_start
    fast = path_start

    # Detect cycle using Floyd's algorithm
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # Cycle detected
            break
    else:
        return None  # No cycle found

    # Find the start of the loop
    slow = path_start
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow.value  # Return the value of the loop start

# Test the function
path_start = Node("Mystic Falls")
waypoint1 = Node("Troll's Bridge")
waypoint2 = Node("Elven Arbor")
waypoint3 = Node("Fairy Glade")

# Create a cycle in the linked list
path_start.next = waypoint1
waypoint1.next = waypoint2
waypoint2.next = waypoint3
waypoint3.next = waypoint1

print(loop_start(path_start))  # Output: "Troll's Bridge"

# ---------------------------------------------------

# Problem 3: Find the Next Highest Scoring Contestant

# Understand:
# - We need to find the next greater node for each node in a linked list.
# - For each node, we need to find the first node after it with a strictly larger value.

# Match:
# - We can solve this using a **monotonic stack** to track nodes while traversing the list.
# - If the current node's value is greater than the value of the node at the top of the stack, update the result.

# Plan:
# 1. Create a Node class to represent each element in the linked list.
# 2. Implement the `next_highest_scoring_contestant` function:
#    - Traverse the list to collect nodes in an array.
#    - Use a stack to track nodes whose next greater value hasn't been found.
#    - For each node, update the result if a greater value is found.
# 3. Test with example lists.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def next_highest_scoring_contestant(head):
    # Collect all nodes into an array
    nodes = []
    current = head
    while current:
        nodes.append(current)
        current = current.next

    # Initialize the result array with 0s
    answer = [0] * len(nodes)
    stack = []  # Stack to store indices of nodes

    # Traverse the nodes and use the stack to find the next greater element
    for i, node in enumerate(nodes):
        while stack and nodes[stack[-1]].value < node.value:
            index = stack.pop()
            answer[index] = node.value  # Update result for the popped index
        stack.append(i)  # Push the current index onto the stack

    return answer

# Test the function
contestant_scores1 = Node(2, Node(1, Node(5)))
contestant_scores2 = Node(2, Node(1, Node(3, Node(5, Node(6, Node(4, Node(7)))))))

print(next_highest_scoring_contestant(contestant_scores1))  # Output: [5, 5, 0]
print(next_highest_scoring_contestant(contestant_scores2))  # Output: [7, 0, 5, 5, 0, 7, 0]

# Problem 5: Grouping Experiments
# Understand:
# - We are given a singly linked list of experiment results, where each result corresponds to an odd or even position.
# - Odd and even positions alternate, starting with the 1st result as odd.
# - We need to reorganize the linked list such that:
#   1. All results in odd positions appear first.
#   2. All results in even positions come after the odd results.
#   3. The relative order of both groups must remain the same as in the original list.

# Match:
# - We'll traverse the linked list once and separate it into two lists: 
#   1. One for odd-positioned results.
#   2. One for even-positioned results.
# - After traversing the list, we merge the two lists.
# - Time complexity: O(n), where n is the length of the list (one pass).
# - Space complexity: O(1), as we only manipulate pointers, without using additional memory.

# Plan:
# 1. Use two pointers: odd_head and even_head, which will point to the start of the odd and even lists, respectively.
# 2. Use two additional pointers: odd_tail and even_tail to build the two lists while traversing.
# 3. Traverse the list while maintaining and updating the odd and even pointers.
# 4. At the end, connect the odd list’s tail to the head of the even list.
# 5. Return the head of the merged list (odd_head).

# Implement:
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def odd_even_experiments(exp_results):
    if not exp_results or not exp_results.next:
        return exp_results  # If the list is empty or has only one element, return as-is.

    # Initialize the odd and even lists
    odd_head = odd_tail = exp_results  # Start from the first (odd) node
    even_head = even_tail = exp_results.next  # Start from the second (even) node

    current = exp_results.next.next  # Start processing from the third node (1-indexed position 3)
    is_odd = True  # Track whether the current node is in an odd or even position

    # Traverse the list and build the odd and even lists
    while current:
        if is_odd:
            odd_tail.next = current  # Append to the odd list
            odd_tail = odd_tail.next
        else:
            even_tail.next = current  # Append to the even list
            even_tail = even_tail.next

        current = current.next  # Move to the next node
        is_odd = not is_odd  # Toggle between odd and even

    # End the even list
    even_tail.next = None
    # Connect the odd list to the even list
    odd_tail.next = even_head

    return odd_head  # Return the head of the reorganized list

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# Example usage:
exp_results = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
print("Original List:")
print_linked_list(exp_results)

reorganized_results = odd_even_experiments(exp_results)
print("\nReorganized List (Odd followed by Even):")
print_linked_list(reorganized_results)