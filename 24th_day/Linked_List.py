#Removing duplicates in a l
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while (start.next != None):
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        # Write your code here
        temp = head
        while temp.next:
            if temp.data==temp.next.data:
                while temp.next and temp.data==temp.next.data:
                    temp.next=temp.next.next
            else:
                temp=temp.next
        return head


mylist = Solution()
T = int(input())
head = None
print("sdf")
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)

mylist.display(head);
print("sdf")
head = mylist.removeDuplicates(head)
print("sdf")
mylist.display(head);