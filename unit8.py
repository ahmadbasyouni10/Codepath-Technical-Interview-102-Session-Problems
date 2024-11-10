class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_flower(root, flower):
    if not root:
        return False
    if root.val == flower:
        return True
    return find_flower(root.left, flower) or find_flower(root.right, flower)

"""
         Rose
        /    \
       /      \
     Lily     Daisy
    /    \        \
Orchid  Lilac    Dahlia
"""

flower_field = TreeNode("Rose", 
                        TreeNode("Lily", TreeNode("Orchid"), TreeNode("Lilac")),
                                TreeNode("Daisy", None, TreeNode("Dahlia")))

print(find_flower(flower_field, "Lilac"))
print(find_flower(flower_field, "Hibiscus"))

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def ocean_depth(root):
    def dfs(node):
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        return max(left, right) + 1
    return dfs(root)

"""
                Sunlight
               /        \
              /          \
          Twilight      Squid
         /       \           \   
      Abyss  Anglerfish    Giant Squid
      /
  Trenches
"""
ocean = TreeNode("Sunlight", 
                TreeNode("Twilight", 
                        TreeNode("Abyss", 
                                TreeNode("Trenches")), TreeNode("Anglerfish")),
                                        TreeNode("Squid", TreeNode("Giant Squid")))

"""
    Spray Zone
    /         \
   /           \ 
Beach       High Tide
            /  
      Middle Tide
              \
            Low Tide
"""
tidal_zones = TreeNode("Spray Zone", 
                      TreeNode("Beach"), 
                              TreeNode("High Tide", 
                                      TreeNode("Middle Tide", None, TreeNode("Low Tide"))))

print(ocean_depth(ocean))
print(ocean_depth(tidal_zones))


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_identical(root1, root2):
    # handles base case if at leaf node and you go left for both or right for both should be true
    # handles if input is both empty nodes
    if not root1 and not root2:
        return True
    # if true here means one of them is null and the other is not means false
    if not root1:
        return False
    if not root2:
        return False
    if root1.val != root2.val:
        return False
    
    return is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right)
    



"""
      1                1
     / \              / \
    2   3            2   3  
"""
root1 = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(1, TreeNode(2), TreeNode(3))

"""
      1                1
     /                  \
    2                    2  
"""

root3 = TreeNode(1, TreeNode(2))
root4 = TreeNode(1, None, TreeNode(2))

print(is_identical(root1, root2))
print(is_identical(root3, root4))



"""
# Example 1

# Input: root = CoralKing
# Expected Output: True

# Example 2

    CoralQueen
     /      \
 CoralX    CoralX
  /  \      /  \
CoralY CoralZ CoralY CoralZ

# Input: root = CoralQueen
# Expected Output: False
"""

def is_symmetric(root):
    def dfs(node1, node2):
        if not node1 and not node2:
            return True
        if not node1:
            return False
        if not node2:
            return False
        if node1.val != node2.val:
            return False
        return dfs(node1.left, node2.right) and dfs(node1.right, node2.left)

    return dfs(root.left, root.right)



"""
        A
      /   \
     B     B
    / \   / \
   C  D   D  C
"""
coral1 = TreeNode('A', 
                  TreeNode('B', TreeNode('C'), TreeNode('D')), 
                          TreeNode('B', TreeNode('D'), TreeNode('C')))


"""
        A
      /   \
     B     B
    / \   / \
   C  D   C  D
"""
coral2 = TreeNode('A', 
                  TreeNode('B', TreeNode('C'), TreeNode('D')), 
                          TreeNode('B', TreeNode('C'), TreeNode('D')))

print(is_symmetric(coral1))
print(is_symmetric(coral2))
