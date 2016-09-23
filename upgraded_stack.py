from stack import Stack


class UpgradedStack(Stack):
    def __init__(self):
        super(Stack, self).__init__()
        self.items = []
        self.__max_stack = Stack()

    def max_val(self):
        if self.__max_stack.is_empty() is False:
            return self.__max_stack.peek()

    def push(self, item):
        if super(UpgradedStack, self).is_empty():
            super(UpgradedStack, self).push(item)
            self.__max_stack.push(item)
        else:
            if item > self.__max_stack.peek():
                super(UpgradedStack, self).push(item)
                self.__max_stack.push(item)
            else:
                super(UpgradedStack, self).push(item)

    def pop(self):
        if super(UpgradedStack, self).pop() == self.__max_stack.peek():
            self.__max_stack.pop()