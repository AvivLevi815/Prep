"""
Node is the building block of a linked list
-- val: value that the Node hlods
-- next: pointer to the next Node in a LinkedList
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

"""
LinkedList is a data structure that holds values in Nodes,
each node is connected to the one after it by a pointer.

This class can create a LinkedList, add a value to it, delete a value from it and print the LinkedList
"""
class LinkedList:
    def __init__(self):
        self.head = None

    # add an element to a LinkedList
    def addElement(self, element):
        if self.head == None:
            self.head = Node(element)
        else:
            curNode = self.head
            while(curNode.next != None):
                curNode = curNode.next
            curNode.next = Node(element)

    # remove an element from a LinkedList
    def removeElement(self, valToRemove):
        if self.head == None:
            return
        curNode = self.head
        while curNode.next.val != valToRemove and curNode.next != None:
            curNode = curNode.next

        if curNode.next.val == valToRemove:
            curNode.next = curNode.next.next
            return
        print("val not found")

    # this function prints a Linked list, for example: [9] --> [1] --> [2] --> [9]
    def printList(self):
        if self.head == None:
            print("Empty LinkedList")
        else:
            curNode = self.head
            while(curNode != None):
                if curNode.next != None:
                    print("[{}] --> ".format(curNode.val), end="")
                else:
                    print("[{}] ".format(curNode.val))

                curNode = curNode.next

# Example usage
myList = LinkedList()
myList.addElement(9)
myList.addElement(1)
myList.addElement(2)
myList.addElement(9)
myList.addElement('94')

myList.removeElement("94")
myList.removeElement(9)
myList.addElement(100)

myList.printList()

