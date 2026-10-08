# Link list 

class node:
  def __init__(self,data):
    self.data = data 
    self.next = None

class Linklist:
  def __init__(self):
    self.head = None
    self.current = None

  def create(self,data):
    if self.head == None:
      self.head = node(data)
      self.current = self.head
    else:
        self.current.next = node(data)
        self.current = self.current.next

  def display(self):
    if self.head == None:
      print("Linklist is empty")
    else:
      counter = self.head
      while counter:
        print(counter.data)
        counter = counter.next

# def main():
ll1 = Linklist()
ll1.create(10)
ll1.create(20)
ll1.create(20)
ll1.display()

# if __name__ == "__main__":
#   main()
      