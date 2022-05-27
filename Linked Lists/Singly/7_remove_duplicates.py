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


    # -------------------------------------Remove Duplicate elements--------------------------------

    # To remove duplicate elemnets we are going to traverse through the list one time and doing so we keep track of
    # data held at each node and we will use a hash table or dictionary to keep track of data elements we found

    def remove_duplicates(self):

        curr = self.head
        prev = None
        # Using a dictionary to keep track of similar elements
        dup_values = dict()

        while curr:
            # If the element already exists in our dictionary we nullify it and point its prev to its next node
            if curr.data in dup_values:
                prev.next = curr.next
                curr = None
            
            # If the element is new we add its count as 1 in dup values indicating it has its occurence now in list
            else:
                dup_values[curr.data] = 1
                prev = curr

            curr = prev.next



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

    # To add new and repetitive elements for testing
    llist.append(5)
    llist.append(1)
    llist.append(4)
    llist.append(2)
    llist.append(6)

    # -----------------REMOVE DUPLICATES--------------------
    llist.remove_duplicates()

    # Prints the list after above operations
    llist.printList()

