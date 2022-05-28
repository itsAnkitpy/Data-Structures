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

    # -------------------------------------Move tail node to head node--------------------------------------

    # For doing this we need to keep track of two nodes:
        # -> The last node because it will point to head node
        # -> The second last node because once last node becomes head it will point to Null

    def move_tail_to_head(self):
        
        # Initializing as Head to traverse throught the list
        last = self.head
        # Keeping track of previous node
        second_to_last = None

        # Till last.next exists run the loop, it will end at second to last node giving us last node
        while last.next:
            second_to_last = last
            last = last.next

        # Pointing last node to head node
        last.next = self.head

        # Pointing second last node to Null
        second_to_last.next = None

        # Finally making last the head node
        self.head = last

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

    # ----------------Move tail to head node--------------------
    llist.move_tail_to_head()
    
    # Prints the list after above operations
    llist.printList()

