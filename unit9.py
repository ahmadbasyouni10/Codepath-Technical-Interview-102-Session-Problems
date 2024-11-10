class TreeNode():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

from collections import deque
def zigzag_icing_order(cupcakes):
    res = []
    left_to_right = True
    queue = deque([cupcakes])
    while queue:
        cur = deque()
        for i in range(len(queue)):
            node = queue.popleft()
            if left_to_right:
                cur.append(node.val)
            else:
                cur.appendleft(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.extend(cur)
        left_to_right = not left_to_right
    return res


"""
            Chocolate
           /         \
        Vanilla       Lemon
       /              /    \
    Strawberry   Hazelnut   Red Velvet   
"""

# Using build_tree() function included at top of page
flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
cupcakes = build_tree(flavors)
print(zigzag_icing_order(cupcakes))


class TreeNode():
     def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

def kth_spookiest(root, k):
    def inorder(node):
        if not node:
            return None
        
        # Traverse the left subtree
        left = inorder(node.left)
        if left is not None:
            return left
        
        # Increment the count when visiting the node
        nonlocal count
        count += 1
        if count == k:
            return node.val
        
        # Traverse the right subtree
        return inorder(node.right)
    
    count = 0
    return inorder(root)

"""
    (3, Lobby) 
   /         \
(1, 101)   (4, 102)
     \
     (2, 201)
"""

# Using build_tree() function at the top of the page
rooms = [(3, "Lobby"), (1, 101), (4, 102), None, (2, 201)]
hotel1 = build_tree(rooms)


"""
            (5, Lobby) 
            /         \
        (3, 101)   (6, 102)
        /      \
    (2, 201)  (4, 202)
    /
(1, 301)
"""
rooms = [(5, 'Lobby'), (3, 101), (6, 102), (2, 201), (4, 202), None, None, (1, 301)]
hotel2 = build_tree(rooms)

print(kth_spookiest(hotel1, 1))
print(kth_spookiest(hotel2, 3))