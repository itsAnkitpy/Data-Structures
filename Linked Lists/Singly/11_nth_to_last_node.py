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


    def length(self):

        curr = self.head
        # Initializing lenght counter as 0
        count = 0

        while curr:
            count += 1
            # Traversing through every element
            curr = curr.next

        return count

    # --------------------------------------Nth to last node----------------------------------------

    def print_nth_from_last(self,n):

        # Method 1:
            # -> First calculate the length of the list
            # -> Then decrement the total length until length == n

        # Calculated length
        total_len = self.length()

        curr = self.head

        while curr:
            # If length is equal to nth node return node
            if total_len == n:
                print(curr.data)
                return curr

            # Else decrement length and move current to next
            total_len -= 1
            curr = curr.next

        if curr is None:
            return

    def nth_from_last(self, n):

        # Method 2:Here we use two pointers P and Q
            # -> P and Q initialized as head nodes
            # -> Q moves n nodes beyond P till it becomes null and P moves steadily
            # -> If we then compare there positions P will be at nth node and Q as said becomes null

        p = self.head
        q = self.head

        count = 0

        # Q moves n nodes beyond P.This is to make Q the fast pointer
        while q and count < n:
            q =  q.next
            count += 1

        if not q:
            print(str(n) + "is greater than number of nodes in the list.")
            return

        while p and q:
            p = p.next
            q = q.next
        
        # In the end P points to nth node and Q is null
        return p.data

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

    llist.append(9)
    llist.append(7)
    llist.append(10)
    llist.append(6)
    llist.append(5)

    # ------------PRINTS NTH TO LAST NODE------------------
    llist.print_nth_from_last(3)
    print(llist.nth_from_last(4))
    
    # Prints the list after above operations
    llist.printList()

