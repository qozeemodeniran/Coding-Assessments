""" 
Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list. Either head pointer may be null meaning that the corresponding list is empty.
"""

def mergeLists(head1, head2):
    dummyNode = SinglyLinkedListNode(0)
    
    last = dummyNode
    while True:
        if head1 is None:
            last.next = head2
            break
        if head1.data <= head2.data:
            last.next = head1
            head1 = head1.next
        else:
            last.next = head2
            head2 = head2.next
        last = last.next
    return dummyNode.next
