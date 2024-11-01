# Question 1
class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_missions(mission1, mission2):
    if not mission1:
        return mission2
    if not mission2:
        return mission1
    if mission1.value < mission2.value:
        mission1.next = merge_missions(mission1.next, mission2)
        return mission1
    else:
        mission2.next = merge_missions(mission1, mission2.next)
        return mission2



mission1 = Node(1, Node(2, Node(4)))
mission2 = Node(1, Node(3, Node(4)))
# 1 1 2 3 3 4

print_linked_list(merge_missions(mission1, mission2))

# Question 1
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_missions_iterative(mission1, mission2):
    temp = Node()  # Temporary node to simplify the merging process
    tail = temp

    while mission1 and mission2:
        if mission1.value < mission2.value:
            tail.next = mission1
            mission1 = mission1.next
        else:
            tail.next = mission2
            mission2 = mission2.next
        tail = tail.next

    # Attach the remaining nodes, if any
    if mission1:
        tail.next = mission1
    elif mission2:
        tail.next = mission2

    return temp.next  # Return the head of the merged linked list

def longest_streak(frames):
    res = -float('inf')
    cur = 0
    for c in frames:
        if c == "S":
            cur += 1
            res = max(res, cur)
        else:
            cur = 0
    return res


print(longest_streak("SSOSSS"))
print(longest_streak("SOSOSOSO"))

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def weave_spells(spell_a, spell_b)
    dummy = Node(0)
    cur = dummy
    while spell_a and spell_b:
        cur.next = spell_a
        cur = cur.next
        cur.next = spell_b
        cur = cur.next
    if spell_a:
        cur.next = spell_a
    if spell_b:
        cur.next = spell_b

spell_a = Node('A', Node('C', Node('E')))
spell_b = Node('B', Node('D', Node('F')))

print_linked_list(weave_spells(spell_a, spell_b))

def decode_scroll_recursive(scroll):
    def decode(index):
        decoded_string = ""
        current_num = 0
        
        while index < len(scroll):
            char = scroll[index]
            
            if char.isdigit():
                # Build the number for the multiplier
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Recurse for the substring inside brackets
                index, decoded_segment = decode(index + 1)
                decoded_string += decoded_segment * current_num
                current_num = 0
            elif char == ']':
                # End of the current recursive segment
                return index, decoded_string
            else:
                # Regular character, just add it to the current string
                decoded_string += char
                
            index += 1
        
        return decoded_string

    # Start decoding from the beginning of the scroll
    return decode(0)[1]

# Test cases
scroll1 = "3[Coral2[Shell]]"
scroll2 = "2[Poseidon3[Sea]]"
print(decode_scroll_recursive(scroll1))  # Expected output: CoralShellShellCoralShellShellCoralShellShell
print(decode_scroll_recursive(scroll2))  # Expected output: PoseidonSeaSeaSeaPoseidonSeaSeaSea

def evaluate_ternary_expression_recursive(expression):
    # Base case: if the expression is a single character, return it
    if len(expression) == 1:
        return expression
    
    # The condition is the first character (either 'T' or 'F')
    condition = expression[0]
    
    # Find the first '?' in the expression (after the condition)
    question_mark_index = 1
    
    # We need to find the matching ':' for this ternary expression
    colon_index = question_mark_index + 1
    balance = 1  # This keeps track of nested ternaries
    
    while balance > 0:
        if expression[colon_index] == '?':
            balance += 1
        elif expression[colon_index] == ':':
            balance -= 1
        colon_index += 1
    
    # The colon_index is now at the character after the correct ':'
    colon_index -= 1
    
    # Extract the true and false expressions
    true_expr = expression[question_mark_index + 1 : colon_index]
    false_expr = expression[colon_index + 1 :]
    
    # Recursively evaluate based on the condition
    if condition == 'T':
        return evaluate_ternary_expression_recursive(true_expr)
    else:
        return evaluate_ternary_expression_recursive(false_expr)