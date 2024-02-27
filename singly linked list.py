class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head

    def addNode(self, val):
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def printLinkedList(self):
        curr = self.head.next
        while curr:
            print(curr.val)
            curr = curr.next
        print()

linkedlist = LinkedList()
linkedlist.addNode(1)
linkedlist.addNode(2)
linkedlist.addNode(3)
linkedlist.printLinkedList()
