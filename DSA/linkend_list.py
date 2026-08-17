class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linklist:

    def __init__(self):
        self.head = None

    def insert_node(self, data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
            return 
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newnode
    
    def insert_start(self, data):
        newnode = node(data)
        temp = self.head

        self.head = newnode
        self.head.next = temp

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end= " -> ")
            temp = temp.next
        print("None")

if __name__ == "__main__":
    ll = linklist()
    ll.insert_node(10)
    ll.insert_node(11)
    ll.insert_node(12)
    ll.insert_node(13)
    ll.insert_node(14)
    ll.insert_node(15)
    ll.insert_start(16)
    ll.display()

