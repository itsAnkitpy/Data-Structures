import os
os.system('cls')

# -----------------------------------Creating a linked list-------------------------------------------------#

# Since each Linked list has Nodes which consist of pointers to next node we create nodes starting of with HEAD node
# and specifying data each node would hold along with what pointers would point to next in the list.

class Node:

    def __init__(self,data):
        # Each node consisting of data and next pointer
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        # Defining the head node of the list
        self.head = None

    def printList(self):
        # Declaring current as head node
        curr = self.head

        # While current node is not None , print the Node data
        while curr:
            print(curr.data, end= " ")
            curr = curr.next


    # --------------------------------Reverse a Linked List-----------------------------------------#

    # Method 1 - Iterative method

    def reverse_iterative(self):

        # To reverse through a list we can iterate throught the list and keep track of previous and current node to 
        # reorient them and swap them

        prev = None
        curr = self.head

        while curr:
            # Swapping operations
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev


    # Method 2 - Recursive method

    def reverse_recursive(self):

        def _reverse_recursive(curr, prev):

            if not curr:
                return prev

            # Swapping operations
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            # Calling it recursively to perform swap operation on each element
            return _reverse_recursive(curr,prev)

        self.head = _reverse_recursive(curr = self.head, prev=None)
            

# Main code to create linked list, adding data to each node and mentioning which node points to which
if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    four = Node(4)

    llist.head.next = second
    second.next = third
    third.next = four

    # ------------REVERSE OPERATIONS----------------
    llist.reverse_iterative()

    llist.reverse_recursive()
    
    # Prints the list after above operations
    llist.printList()

