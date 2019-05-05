class Stack:

    def __init__(self, initial_size = 10):
        self.arr = [0 for x in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0
    
    def push(self, value):

        #check if capacity is full
        if self.next_index == len(self.arr):
            self.handle_full_capacity()

        self.arr[self.next_index] = value
        self.next_index += 1
        self.num_elements += 1

    def handle_full_capacity(self):
        old_arr = self.arr

        self.arr = [0 for x in range(2 * len(self.arr))]
        for index, value in enumerate(old_arr):
            self.arr[index] = value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.next_index == 0

    