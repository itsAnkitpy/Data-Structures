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

    # ---------------------------------Calculating Length of Linked List---------------------------------#

    # Method 1 - Iterative method

    def len_iterative(self):

        curr = self.head
        # Initializing lenght counter as 0
        count = 0

        while curr:
            count += 1
            # Traversing through every element
            curr = curr.next

        return count

    # Method 2 - Recursive method

    def len_recursive(self, node):

        if node is None:
            return 0
        # Traversing through every element
        return 1 + self.len_recursive(node.next)


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

    #--------- CALCULATE LENGTH OPERATIONS---------
    print(llist.len_iterative())
    print(llist.len_recursive(llist.head))
    
    # Prints the list after above operations
    llist.printList()

