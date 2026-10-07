# create a singly link list
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None


class Linklist:
  def __init__(self):
    self.Head = None
    self.current = None
    print("---Link list ---")

  def create(self,data):
    if self.Head is None:
      self.Head = Node(data)
      self.current = self.Head
    else:
      self.current.next = Node(data)
      self.current = self.current.next

  def display(self):
    if self.Head == None:
      print("linkList is empty")
    else:
      disp = self.Head
      while disp:
        print(disp.data)
        disp = disp.next

linklist1 = Linklist()

linklist1.create(1)
linklist1.create(2)
linklist1.create(3)


linklist1.display()