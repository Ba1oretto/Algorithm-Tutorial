from utils import StaticArray


class DynamicArray(StaticArray):
    def __init__(self, size, isSet=False):
        super(DynamicArray, self).__init__(size)
        self.isSet = isSet
        self.isResizing = False

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        # set: check whether value is present
        if self.isSet and self.argwhere(value).__len__() != 0:
            return
        if index >= self.__len__():
            super().__setitem__(self.__len__(), value)
        else:
            i = self.__len__()
            while i > index:
                super().__setitem__(i, self[i - 1])
                i -= 1
            super().__setitem__(index, value)

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
        self[self.__len__()] = value

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
        arr_copy = StaticArray(self.size)
        for element in self.data:
            arr_copy.append(element)

        # resize array
        self.resize(size)

        # copy to new array
        for element in arr_copy:
            self.append(element)

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
