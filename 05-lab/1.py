class SinglyLinkedListBase:
  def __init__(self):
    self._count = 0
    self._head = None

class DataNode:
  def __init__(self, name, next):
    self._name = name
    self._next = next

  def __str__(self):
    return self._name

class SinglyLinkedList(SinglyLinkedListBase):
    def traverse(self):
      current = self._head
      if self._head is None:
        print("This is an empty list.")
      else:
        while current._next is not None:
          print(current._name, end=' -> ')
          current = current._next
        print(current._name)
      pass

    def insertFront(self, data):
      pNew = DataNode(data, None)
      if self._head is None:
        self._head = pNew
      else:
        pNew._next = self._head
        self._head = pNew
      self._count += 1

    def insertLast(self, data):
      pNew = DataNode(data, None)
      if self._head is None:
        self._head = pNew
      else:
        current = self._head
        while current._next is not None:
            current = current._next
        current._next = pNew
      self._count += 1

    def insertBefore(self, node_name, data):
      pNew = DataNode(data, None)
      if self._head is None:
        print('This is empty linked list')
        return

      if str(self._head) is node_name:
        pNew._next = self._head
        self._head = pNew
        self._count += 1
        return

      current = self._head
      while current._next is not None and current._next._name != node_name:
        current = current._next

      if current._next is None:
        print(f'Node with data {node_name} not found')
      else:
        pNew._next = current._next
        current._next = pNew
        self._count += 1


    def delete(self, data_):
      if self._head is None:
        print("This is an empty list.")
        return

      if self._head._name == data_:
        self._head = self._head._next
        self._count -= 1
        return

      current = self._head
      while current._next is not None and current._next._name != data_:
        current = current._next

      if current._next is None:
        print(f"Node with data '{data_}' not found.")
      else:
        current._next = current._next._next
        self._count -= 1



    def getSize(self):
      return self._count
  
list1 = SinglyLinkedList()
list1.traverse()
list1.insertBefore("Kim", "Ko")

print("Add John...")
list1._head = DataNode("John", None)
list1._count += 1

print("Head node is: " + list1._head._name)
print(f"Node count: {list1.getSize()}")
list1.traverse()

print("Add Tony...")
pNew = DataNode("Tony", None)
print("Address of Node-Tony: ", hex(id(pNew)))
list1._head._next = pNew
print("Value of list1.head.next: ", list1._head._next)
list1._count += 1

print(f"Next node is: {list1._head._next._name}")
print(f"Node count: {list1.getSize()}")

list1.traverse()

print("Add Bill...")
pNew = DataNode("Bill", None)
list1._head._next._next = pNew
list1._count += 1

print(f"Next node is: {list1._head._next._name}")
print(f"Node count: {list1.getSize()}")

list1.traverse()
list1.insertFront("Kim")
list1.traverse()

list1.insertLast("Max")
list1.traverse()

list1.insertBefore("Tony", "Andy")
list1.traverse()

list1.insertBefore("Kimmy", "Mike")
list1.traverse()

list1.insertBefore("Kim", "Boyz")
list1.traverse()

list1.delete("Kim")
list1.traverse()

list1.delete("Boyz")
list1.traverse()