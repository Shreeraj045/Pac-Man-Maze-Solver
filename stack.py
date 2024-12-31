class Stack:
    # You can implement this class however you like
    def __init__(self):
        #YOU CAN (AND SHOULD!) MODIFY THIS FUNCTION
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self,element):
        self._data.append(element)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self._data[-1]
        
    def pop(self):
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self._data.pop()

#Credits - Class Notes - © 2021 Goodrich, Tamassia, Goldwasser Stacks