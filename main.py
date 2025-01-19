from Lists.simple_list import SimpleLinkedList
from Lists.doubly_list import DoublyLinkedList
from Lists.circular_list import CircularList
from Lists.header_linked_list import HeaderNodeList

list = HeaderNodeList("ummed")
list.append(10)
list.append(20)
list.append(30)
list.append(40)
list.append(50)
list.display()
list.delete_node_x(10)
list.display()

