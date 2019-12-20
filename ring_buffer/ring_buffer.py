from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):

        if self.storage.length < self.capacity:
            self.storage.add_to_head(item)
            self.current = self.storage.tail
        else:
            self.current.value = item
            self.current = self.current.prev


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current_item = self.storage.tail
        while current_item is not self.storage.head:
            list_buffer_contents.append(current_item.value)
            current_item = current_item.prev
        list_buffer_contents.append(self.storage.head.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
