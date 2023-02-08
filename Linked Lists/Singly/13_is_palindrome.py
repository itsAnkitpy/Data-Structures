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


    # ---------------------------------------IS PALINDROME---------------------------------------------

    def is_palindrome(self):

        # Method 1 - Using reverse slicing
        # s = ""
        # p = self.head

        # # Storing every value in s and comparing it with reverse
        # while p:
        #     s += p.data
        #     p = p.next

        # return s == s[::-1]

        # Method 2 - Using Stack

        # p = self.head
        # s = []

        # # To store every element of our given string in stack
        # while p:
        #     s.append(p.data)
        #     p = p.next
        
        # # Reinitializing p as head again for second time to run it from head for comparing
        # p = self.head

        # while p:
        #     # Since stack follows LIFO Operation it will pop the last entered element
        #     data = s.pop()

        #     # Comparing p data with the reverse data obtained from stack
        #     if p.data != data:
        #         return False

        #     p = p.next

        # return True


        # Method 3 - In this method we use two pointers - P and Q
        # P will point to the head node and Q will point to the last node.
        # For P we will move forward and for Q we will move in reverse and compare data of them simultaneously.
        # We do it until we get to a point where they meet or cross each other i.e mid

        p = self.head
        q = self.head

        # To store values of our data as q data
        prev = []

        i = 0

        while q:
            prev.append(q.data)
            q.next
            i += 1

        count = 1

        while count <= i // 2 + 1:

            if prev[-count].data != p.data:
                return False

            prev.next
            count += 1

        return True



# Main code to create linked list, adding data to each node and mentioning which node points to which
if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node("A")
    second = Node("B")
    third = Node("B")
    four = Node("A")

    llist.head.next = second
    second.next = third
    third.next = four

    print(llist.is_palindrome())

    llist.printList()

