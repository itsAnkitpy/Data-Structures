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

    # ---------------------------------SWAPPING TWO NODES-------------------------------------------#
    # This process also has two cases.
        # 1. When node 1 and node 2 are not head nodes
        # 2. When node 1 and node 2 are head nodes

    def swap_nodes(self, key_1, key_2):
        
        # If the value of both nodes is same there is no point swapping
        if key_1 == key_2:
            return

        # Initializing previous node and current node for traversing - to find key_1
        prev_1 = None
        curr_1 = self.head

        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        # Initializing previous node and current node for traversing - to find key_2
        prev_2 = None
        curr_2 = self.head

        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        # If key_1 and key_2 don't exist
        if not curr_1 or not curr_2:
            return

        # Main code for swap operation
        
        # When node1 is not head node
        if prev_1:
            prev_1.next = curr_2
        # When node1 is head node
        else:
            self.head = curr_2


        # When node2 is not head node
        if prev_2:
            prev_2.next = curr_1
        # When node2 is head node
        else:
            self.head = curr_1

        # Finally swapping their next pointer values so that other elements remain in their respective position
        curr_1.next, curr_2.next = curr_2.next, curr_1.next

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

    #--------- SWAP OPERATIONS---------
    # Swaps nodes with data 2 and 4
    llist.swap_nodes(2,4)
    # Swaps nodes with data 2 and 4
    llist.swap_nodes(1,3)
    
    # Prints the list after above operations
    llist.printList()

