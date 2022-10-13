from programming_assignment_1.assignment_syllabus.utils import Node, Collections, StaticArray


class LinkedList(Collections):
    def __init__(self, isSet=False, isDoubly=False, isCircular=False):
        super(LinkedList, self).__init__()
        self.head: Node = None
        self.isSet = isSet
        self.isDoubly = isDoubly
        self.isCircular = isCircular
        self.tail: Node = None

    def should_break(self, node):
        return self.isCircular and node is self.head

    def __getitem__(self, index):
        if index > self.get_size():
            raise IndexError
        elif index == 0:
            return self.head
        elif index == self.get_size():
            return self.tail
        else:
            ret = self.head
            while index:
                ret = ret.next
                index -= 1
            return ret

    def __setitem__(self, index, value):
        # set: check duplicate
        current = self.head
        if self.isSet:
            while current is not None:
                if current.data == value:
                    return
                current = current.next
                if self.should_break(current):
                    break
        # set value
        node = Node(value)
        # insert to index 0 or list is empty
        if index == 0 or self.get_size() == 0:
            node.next = self.head
            self.head = node
            # list has only 1 element: update tail and the 'next' property
            if self.isCircular and self.tail is not None:
                self.tail.next = self.head
            if self.get_size() == 1:
                self.tail = self.head
                if self.isCircular:
                    self.tail.next = self.head
            if self.isDoubly:
                self.head.prev = self.tail
                if self.head.next is not None:
                    self.head.next.prev = self.head
        elif index >= self.get_size():
            self.tail.next = node
            if self.isDoubly:
                node.prev = self.tail
                self.head.prev = node
            self.tail = node
            if self.isCircular:
                self.tail.next = self.head
        else:
            i = index
            current = self.head
            while i - 1:
                current = current.next
                i -= 1
            node.next = current.next
            current.next = node
            if self.isDoubly:
                node.prev = current
                node.next.prev = node

    def __delitem__(self, index):
        if index > self.get_size():
            raise IndexError
        elif index == 0:
            # should update head.prev and tail.next
            node = self.head.next
            if node is not None:
                if self.isDoubly:
                    node.prev = self.head.prev
                if self.isCircular:
                    self.tail.next = node
            self.head = node
        else:
            current = self.head
            i = index
            while i - 1:
                current = current.next
                i -= 1
            node = current.next.next
            current.next = self.head if self.isCircular and index == self.get_size() - 1 else node
            if index == self.get_size():
                self.tail = current
                if self.isDoubly:
                    self.head.prev = self.tail

            if self.isDoubly:
                node.prev = current

    def append(self, value):
        self[self.get_size()] = value

    def extend(self, arr):
        for element in arr:
            self.append(element)

    def remove(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.data == value:
                del self[index]
                break
            current = current.next
            index += 1

    def argwhere(self, value):
        current = self.head
        count = 0
        while current is not None:
            if current.data == value:
                count += 1
            current = current.next
            if self.should_break(current):
                break

        ret = StaticArray(count)
        index = 0
        current = self.head
        while current is not None:
            if current.data == value:
                ret.append(index)
            index += 1
            current = current.next
            if self.should_break(current):
                break
        return ret

    def __len__(self):
        current = self.head
        count = 0
        while current is not None:
            current = current.next
            count += 1
            # break loop if turn to head
            if self.should_break(current):
                break
        return count

    def get_size(self):
        return self.__len__()

    def __eq__(self, arr):
        if self.__class__ is not arr.__class__ or self.get_size() != arr.get_size():
            return False
        current = self.head
        index = 0
        while current is not None:
            if current.data != arr[index].data:
                return False
            current = current.next
            index += 1
            if self.should_break(current):
                break
        return True

    def __repr__(self):
        current = self.head
        ret = StaticArray(self.get_size())
        while current is not None:
            ret.append(current.data)
            current = current.next
            if self.should_break(current):
                break
        return f"{ret}"

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next
            if self.should_break(current):
                break


if __name__ == '__main__':
    pass
