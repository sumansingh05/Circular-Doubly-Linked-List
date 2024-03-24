class Node:
    def __init__(self,data):
        self.item = data
        self.prev = None
        self.next = None

class CDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None
    
    #searching a node is present in circular doubly linked list
    def search(self,data):
        current = self.head
        while current is not self.tail:
            if(current.item == data):
                return current
            current = current.next
            if current == self.tail:
                if(current.item == data):
                    return current
        return None     
    
    
    #inserting a newNode at the starting of the Circular Doubly linked list
    def insertAtFirst(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
            newNode.prev = newNode  
            newNode.next = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            newNode.prev = self.tail
            self.tail.next = newNode
            self.head = newNode

    #inserting a newNode at the last of the Circular Doubly linked list
    def insertAtLast(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
            newNode.prev = newNode  
            newNode.next = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode 
            newNode.next = self.head
            self.head.prev = newNode           
            self.tail = newNode

    #insert a node inside a circular doubly linked list after a current node
    def insertInside(self,current,data):
        if current is None:
            print("Node is not find in the list!")
            return
        else:
            newNode = Node(data)
            if current.item is self.tail.item:
                self.insertAtLast(data)
            else:
                newNode.next = current.next
                newNode.prev = current
                current.next.prev=newNode
                current.next=newNode  

    #delete a first node inside a circular Doubly Linked List
    def deleteFirst(self):
        if self.is_empty():
            print("Circular Doubly Linked List is empty!")
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head           


    #delete a last node inside a circular Doubly Linked List
    def deleteLast(self):
        if self.is_empty():
            print("Circular Doubly Linked List is empty!")
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                current = self.head
                while current.next is not self.tail:
                    current = current.next
                current.next = self.head
                self.head.prev = current
                self.tail = current    

    
    #delete a last node inside a circular Doubly Linked List
    def deleteInside(self,data):
        if self.is_empty():
            print("Circular Doubly Linked List is empty!")
        else:
            if self.head.item == data:
                self.deleteFirst()
            elif self.tail.item == data:
                self.deleteLast()
            else:
                current = self.head
                while current is not self.tail:
                    if current.item == data:
                        current.prev.next = current.next
                        current.next.prev = current.prev
                        return                        
                    current = current.next

            
    #function to display the circular doubly linked list          
    def display(self):
        current = self.head                                                                                                                     
        print("Circular Doubly Linked List is:",end=" ")
        while(current):
            print(current.item,end=" ")
            current = current.next            
            if current is self.head:
                break


list = CDLL()
list.insertAtFirst(11) 
list.insertAtFirst(1) 
list.insertAtLast(100)
list.insertInside(list.search(100),200)
list.display()
print()
print("Head of Circular Doubly Linked List ",list.head.item)
print("Tail of Circular Doubly Linked List ",list.tail.item)
print(list.head.prev.item)
list.deleteInside(1)
list.display()
print()
print("Head of Circular Doubly Linked List ",list.head.item)
print("Tail of Circular Doubly Linked List ",list.tail.item)
print(list.head.prev.item)
list.deleteInside(100)
list.display()
print()
print("Head of Circular Doubly Linked List ",list.head.item)
print("Tail of Circular Doubly Linked List ",list.tail.item)
print(list.head.prev.item)

    

