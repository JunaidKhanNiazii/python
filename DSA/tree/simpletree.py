
print (" -- Binary Tree -- ")

#             root
#            /     \ 
#         child1    child2
#
#
#
class node:
  def __init__(self, data):
    self.data = data
    self.left = None 
    self.right = None

root = node(20)
child1 = node (30)
child2 = node (40)

root.left = child1
root.right = child2

print(root.data)
print(root.left.data)
print(root.right.data)

