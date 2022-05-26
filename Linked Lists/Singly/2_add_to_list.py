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

    # ------------------------------------ADD TO LINKED LIST-----------------------------------------#
    # There are 3 ways to insert a node in the list
        # 1. At the front of the list- Prepend
        # 2. At the given position or after certain node
        # 3. At the end - Append

    # Method 1 - To add in the front 
    def prepend(self, new_data):
        
        # Declaring the new node with its data
        new_node = Node(new_data)

        # Declaring new node's pointer which is the existing head
        new_node.next = self.head

        # Finally assigning new head value to new node
        self.head = new_node



    # Method 2 - TO insert after given node
    def insert_after(self, prev_node, new_data):

        # Check if previous node even exists first
        if prev_node is None:
            print("The given previous node does not exist in the list")
            return

        # Declaring the new node with its data
        new_node = Node(new_data)

        # Declaring new node's pointer which is the next of previous node
        new_node.next = prev_node.next

        # Finally pointing prev node to new node
        prev_node.next = new_node


    # Method 3 - To add at the end
    def append(self, new_data):

        # Declaring the new node with its data
        new_node = Node(new_data)

        # In case the list is empty we make new node our head node 
        if self.head is None:
            self.head = new_node
            return

        curr = self.head

        # While there are nodes which don't point to none we traverse through the list to reach the end of the list
        while curr.next:
            curr = curr.next

        # When we reach the end just assign the new node to existing last node of the list
        curr.next = new_node

        

    

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

    #--------- ADD OPERATIONS-------
    # Adds 0 to the head of the list
    llist.prepend(0)
    # Adds 4.5 after 4 in the list
    llist.insert_after(0, 4.5)
    # Adds 5 to the end of the list
    llist.append(5)

    # Prints the list after above operations
    llist.printList()

