from programming_assignment_1.assignment_syllabus.utils import StaticArray


def append_value(arr, value):
    index = 0
    for e in arr:
        if e is None:
            arr[index] = value
            break
        index += 1


class DynamicArray(StaticArray):
    def __init__(self, size, isSet=False):
        super(DynamicArray, self).__init__(size)
        self.isSet = isSet

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        # check whether value is present
        if self.isSet and self.argwhere(value).__len__() != 0:
            return

        # case: append
        if self[index] is None:
            pointer = 0
            for e in self:
                if e is None:
                    super().__setitem__(pointer, value)
                    break
                pointer += 1
            return
        # case: shift
        else:
            current_index = self.__len__()
            while True:
                if current_index == 0:
                    super().__setitem__(index, value)
                    break
                super().__setitem__(current_index, self[current_index - 1])
                current_index -= 1

        # resize array
        self.resize_array()

    def __delitem__(self, index):
        # delete element
        while True:
            if index is self.size - 1 or index is self.__len__() or self.data[index] is self.data[index + 1] is None:
                break
            self.data[index] = self.data[index + 1]
            self.data[index + 1] = None
            index += 1

        # resize array
        self.resize_array(True)

    def append(self, value):
        index = 0
        for element in self:
            if element is None:
                self[index] = value
                break
            index += 1

        self.resize_array()

    def extend(self, arr):
        for element in arr:
            self.append(element)

    def remove(self, value):
        super().remove(value)

    def argwhere(self, value):
        return super().argwhere(value)

    def __len__(self):
        count = 0
        for element in self.data:
            if element is not None:
                count += 1
        return count

    def get_size(self):
        return self.size

    def __eq__(self, arr):
        length = arr.__len__()
        if self.__class__ == arr.__class__:
            index = 0
            while index < length:
                if self.data[index] != arr[index]:
                    return False
                index += 1
            return True
        return False

    def __repr__(self):
        return f"{self.data}"

    def __iter__(self):
        for element in self.data:
            yield element

    def reallocate(self, size):
        # backup array
        arr_copy = DynamicArray(self.size)
        for element in self.data:
            append_value(arr_copy, element)

        # resize array
        self.resize(size)

        # copy to new array
        for element in arr_copy:
            append_value(self, element)

    def resize(self, size):
        """
        Do not modify this function.
        This function will enable you to resize your structure.
        This function is destructive! Be careful.
        """
        self.data = [None] * size
        self.size = size

    def resize_array(self, decrease=False):
        if self.__len__() / self.size < 0.2 and decrease:
            self.reallocate(self.size // 2)
        elif self.__len__() / self.size > 0.8:
            self.reallocate(self.size * 2)


if __name__ == '__main__':
    pass
