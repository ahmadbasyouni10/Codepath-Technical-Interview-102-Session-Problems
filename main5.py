# Problem: Print Elements from a Linked List

# Understand:
# - We need to traverse a linked list and print its elements in order.
# - Each node stores a value and a reference to the next node.
# - If a node doesn’t have a next reference, it marks the end of the list.

# Match:
# - We can solve this by iterating through the linked list starting from the head node.
# - We collect the node values in a list and join them with " -> " to match the required output format.

# Plan:
# 1. Create a Node class to represent each element in the linked list.
# 2. Implement a print_list function that:
#    - Iterates through the list, collecting node data into a result list.
#    - Joins the data using " -> " as a separator.
# 3. Create three linked nodes: Isabelle -> Saharah -> C.J.
# 4. Use print_list to print the entire list starting from the first node.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(node):
    res = []
    while node:
        res.append(node.data)
        node = node.next
    return " -> ".join(res)
    

isabelle = Node("Isabelle")
saharah = Node("Saharah")
cj = Node("C.J.")

isabelle.next = saharah
saharah.next = cj
print(print_list(isabelle))


# Question 2


dog = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
cheese = Node("Gouda")

dog.next = cat
cat.next = mouse
mouse.next = cheese

def chase_list(node):
    res = []
    while node:
        res.append(node.data)
        node = node.next
    return ' chases '.join(res)

print(chase_list(dog))

# Question 3 
# Understand:
# - We need to model a linked list of fish names.
# - Each node represents a fish, and it points to the next fish in the list.
# - The goal is to implement a function `restock` that adds a new fish at the end of the list.

# Match:
# - This is a linked list problem where we traverse the list and modify the tail by adding a new node.
# - We’ll also implement a function to print the fish names, separated by " -> ".

# Plan:
# 1. Define the `Node` class to represent each fish, with `fish_name` and a reference to the next node.
# 2. Implement `print_linked_list` to print the fish names in sequence.
# 3. Implement `restock` to add a new fish at the end of the list.
# 4. Create a test linked list: Carp -> Dace -> Cherry Salmon.
# 5. Use `restock` to add "Rainbow Trout" to the end.
# 6. Print the final list to confirm the new fish is added.
class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def restock(head, new_fish):
    new = Node(new_fish)
    cur = head
    while cur.next is not None:
        cur = cur.next
    cur.next = new


fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
restock(fish_list, "Rainbow Trout")
print_linked_list(fish_list)


# Question 4
class Node:
    def __init__(self, player, next=None):
        self.player_name = player
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.player_name, end=" -> " if current.next else "\n")
        current = current.next

def increment_rank(head, target):
    if target <= 1 or head is None or head.next is None:
        return None
    
    prev = None
    cur = head
    index = 1

    while index < target:
        prev = cur
        cur = cur.next
        index += 1
    tmp = prev.player_name
    prev.player_name = cur.player_name
    cur.player_name = tmp

    return head
        
    




racers1 = Node("Mario", Node("Peach", Node("Luigi", Node("Daisy"))))
racers2 = Node("Mario", Node("Luigi"))

print_linked_list(increment_rank(racers1, 3))
print_linked_list(increment_rank(racers2, 1)) 
print_linked_list(increment_rank(None, 1)) 
