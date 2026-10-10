# pre order traversal 

class node: 
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None
# Creating tree 
five = node(5)
three = node(3)
four = node(4)
two = node(2)
nine = node(9)
eight = node(8)
ten =  node(10)
one = node(1)
six = node(6)

five.left = three
five.right = four

three.left = two
three.right = nine

four.left = eight 
four.right = ten

eight.left = one
eight.right = six


# print(five.data)
# print(five.left.data)
# print(five.right.data)



# preorder traversal
def preorder_traversal (node):
  if node == None:
    return
  print(node.data, end = " ")
  preorder_traversal(node.left)
  preorder_traversal(node.right)
  
preorder_traversal(five)