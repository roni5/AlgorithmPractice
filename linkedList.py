# Is there a cycle?
class SingleNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def cycle_check(node):
    visited_node = [node]
    while node.next != None:
        if node.next in visited_node:
            return True
        else:
            visited_node.append(node.next)
            node = node.next
    return False

def cycle_check2(node):
    marker1 = node
    marker2 = node
    while marker2 != None and marker2.next != None:
        marker1 = marker1.next
        marker2 = marker2.next.next
        if marker1 == marker2:
            return True
    return False

a = SingleNode(1)
b = SingleNode(2)
c = SingleNode(3)
a.next = b
b.next = c
c.next = a

x = SingleNode(2)
y = SingleNode(3)
z = SingleNode(4)
x.next = y
y.next = z

print('--single node cycle--', cycle_check(a))
print('--single node cycle--', cycle_check(x))
print('--single node cycle--', cycle_check2(a))
print('--single node cycle--', cycle_check2(x))

# Input head node and reverse and return new head
def reverse_node(node):
    current = node
    next = None
    previous = None
    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next

    return previous

# Return nth last value in the linked list given head
def nth_last(n, head):

    left_pointer = head
    right_pointer = head

    for i in range(n-1): # separate left and right by n steps
        if right_pointer.next == None:
            raise LookupError('too small list')

        right_pointer = right_pointer.next

    while right_pointer.next:
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next

    return left_pointer

q = SingleNode(1)
w = SingleNode(2)
e = SingleNode(3)
r = SingleNode(4)
t = SingleNode(5)

q.next = w
w.next = e
e.next = r
r.next = t

print(nth_last(2,q).value)



