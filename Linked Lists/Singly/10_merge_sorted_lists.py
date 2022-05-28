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

    # --------------------------------------Merge Two Sorted Lists--------------------------------------

    # Here we will use 3 pointers:
        # P for going through list1
        # Q for going through list2
        # S for keeping track of lesser value among two lists when we compare them 

    # Here second list is passed as llist 
    def merge_sorted_lists(self,llist):

        p = self.head
        q = llist.head
        s = None

        # If p is empty
        if not p:
            return q
        # If q is empty
        if not q:
            return p

        # To detemine where S points first we compare P and Q values. S will point to lesser value of the two.
        if p and q:
            if p.data <= q.data:
                # S moves to P and P moves to next node
                s = p
                p = s.next

            else:
                # S moves to Q and Q moves to next node
                s = q
                q = s.next

            new_head = s

        while p and q:
            # If S is currently at Q and now P has lesser value it moves to P again
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            
            # If S is currently at P and now Q has lesser value it moves to Q again
            else:
                s.next = q
                s = q
                q = s.next

        # If list p has ran out of elements 
        if not p:
            s.next = q

        # If list q has ran out of elements
        if not q:
            s.next = p

        # Return new_head sorted from lesser to higher values
        return new_head

# Main code to create linked list, adding data to each node and mentioning which node points to which
if __name__ == "__main__":
    llist_1 = LinkedList()
    llist_2 = LinkedList()

    # Adding elements to list1 in sorted way
    llist_1.append(1)
    llist_1.append(5)
    llist_1.append(7)
    llist_1.append(9)
    llist_1.append(10)
    # Adding elements to list2 in sorted way
    llist_2.append(2)
    llist_2.append(3)
    llist_2.append(4)
    llist_2.append(6)
    llist_2.append(8)

    # -----------MERGE SORTED OPERATION------------
    llist_1.merge_sorted_lists(llist_2)


    llist_1.printList()

