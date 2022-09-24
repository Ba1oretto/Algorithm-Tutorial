from utils import StaticArray

class DynamicArray(StaticArray):
    def __init__(self, size, isSet = False):
        super(DynamicArray,self).__init__(size)
        pass
        
    def __getitem__(self, index):
        pass

    def __setitem__(self, index, value):
        pass

    def __delitem__(self, index):
        pass

    def append(self, value):
        pass

    def extend(self, arr):
        pass

    def remove(self, value):
        pass

    def argwhere(self, value):
        pass

    def __len__(self):
        pass

    def get_size(self):
        pass

    def __eq__(self, arr):
        pass

    def __repr__(self):
        pass #Not required but useful for debugging

    def __iter__(self):
        pass

    def reallocate(self, size):
        pass

    def resize(self, size):
        """
        Do not modify this function.
        This function will enable you to resize your structure.
        This function is destructive! Be careful.
        """
        self.data = [None]*size
        self.size = size