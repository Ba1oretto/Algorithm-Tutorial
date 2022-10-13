from programming_assignment_1.section_2.arrays import DynamicArray
from programming_assignment_1.section_3.linkedlist import LinkedList


class StackOrQueue:
    def __init__(self, useLinkedList=False, isQueue=False):
        self.data = LinkedList() if useLinkedList else DynamicArray(5)
        self.useLinkedList = useLinkedList
        self.isQueue = isQueue

    def peek(self):
        return self.data[self.data.__len__() - 1] if self.isQueue else self.data[0]

    def push(self, value):
        self.data[0] = value

    def pop(self):
        index = self.data.__len__() - 1 if self.isQueue else 0
        ret = self.data[index]
        del self.data[index]
        return ret

    def __repr__(self):
        return self.data.__repr__()


if __name__ == '__main__':
    adt = StackOrQueue(useLinkedList=True, isQueue=True)
    adt.push('A')
    adt.push('B')
    print(adt.peek().data)
