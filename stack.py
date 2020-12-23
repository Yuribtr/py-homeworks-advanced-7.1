class Stack:
    def __init__(self, *args):
        self.__data = [*args]

    def isEmpty(self):
        return len(self.__data) > 0

    def push(self, obj):
        self.__data.insert(0, obj)

    def pop(self):
        return self.__data.pop(0)

    def peek(self):
        if len(self.__data) > 0:
            return self.__data[0]

    def size(self):
        return len(self.__data)

    # def __next__(self):
    #     return self.__data.pop()
    #
    # def __iter__(self):
    #     return self.__data.__iter__()
