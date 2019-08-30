class Stack:

    def __init__(self):
        """__init__ is used to establish baseline of calss for each instantiation"""
        self.items = []

    def push(self, item):
        """take the item passed as an argument and append to end of list"""
        self.items.append(item)

    def pop(self):
        """return and Remove the last element from the Stack, items does this natively"""
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """look at the last item on the stack, without removing"""
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """Return the length of the stack"""
        return len(self.items)

    def is_empty(self):
        """Return true or false if there are any items in the list"""

        return self.items == []
