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


    # ------------------------------------DELETION IN A LINKED LIST-----------------------------------------#
    # There are 2 ways of deletion:
        # 1. Deleting using data
        # 2. Deleting using its position

    # Method 1 - Deleting using data

    def delete_node(self, key):

        cur_node = self.head

        # Case 1 - If node is head which is to be deleted

        if cur_node and cur_node.data == key:
            # Make the next node of it as head
            self.head = cur_node.next
            # Assign it null value so it becomes of no use which means its deleted
            cur_node = None
            return

        # Case 2 - If node is not head. In this case we need to keep track of previous nodes also.

        prev_node = None
        # To find the node to be deleted we traverse through the list
        while cur_node and cur_node.data != key:
            prev_node = cur_node
            cur_node = cur_node.next

        # If the list is empty to begin with
        if cur_node is None:
            return 

        # Finally after finding the element assign pointer values of previous node to cur_node.next
        prev_node.next = cur_node.next

        # Assign it null value so it becomes of no use which means its deleted
        cur_node = None


    # Method 2 - Deleting using its position

    def delete_node_at_pos(self, pos):

        cur_node = self.head

        # Case 1 - If position is head which is to be deleted

        if pos == 0:
            self.head = cur_node.next
            return

        # Case 2 - If position is not of head node

        prev_node = None
        count = 0

        while cur_node and count != pos:
            prev_node = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return

        prev_node.next = cur_node.next
        cur_node = None






        


# Main code to create linked list, adding data to each node and mentioning which node points to which
if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)

    llist.head.next = second
    second.next = third
    third.next = four
    four.next = five
    five.next = six

    #--------- DELETE OPERATIONS---------
    # Deletes nodes with data 2 and 6
    llist.delete_node(2)
    llist.delete_node(6)

    # Deletes node at position 2 after above operations
    llist.delete_node_at_pos(2)


    # Prints the list after above operations
    llist.printList() 

