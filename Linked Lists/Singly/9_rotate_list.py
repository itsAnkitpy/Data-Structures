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


    # ----------------------------------Rotate List-------------------------------------------------#

    # We can do this by using two pointers - P and Q
    # We will initialize them as HEAD and move along the list nodes in a way that P moves till kTH node and at that 
    # point Q should be at last node of the list
    # Q then points to head node,head points to P's next node and finally P points to None to mark the end of list.

    def rotate(self,k):
        # Initialize them as heads
        p = self.head
        q = self.head

        prev = None
        count = 0

        # Moving pointer P till kth node
        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count += 1

        p = prev

        # Moving pointer Q till last node of the list
        while q:
            prev = q
            q =  q.next

        q = prev

        # Changing pointers of nodes

        # Q points to self.head
        q.next = self.head

        # HEAD itself points to new head which would be the P's next node
        self.head = p.next

        # P now should point to None as it marks the end of list
        p.next= None

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

    llist.append(8)
    llist.append(11)
    llist.append(7)

    # ---------ROTATE OPERATIONS---------------
    llist.rotate(2)

    llist.printList()

