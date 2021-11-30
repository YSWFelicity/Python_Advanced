'''
Sample Code
CS 5001, Fall 2021 - Lecture 10
An implementation of the Queue ADT.
'''


class Queue:
    '''
        Class -- Queue
            A queue data structure.
        Attributes:
            items -- A list of items stored in the queue.
        Methods:
            enqueue -- Adds an item to the queue.
            dequeue -- Returns and removes the item at the front of the queue.
            is_empty -- Check if the queue is empty
            size -- Return the number of items in the queue
    '''

    def __init__(self):
        '''
            Constructor -- creates a new instance of the Queue class.
            Parameters:
                self -- the current Queue object.
        '''        
        self.items = []

    def enqueue(self, item):
        '''
            Method -- enqueue
                Adds an item to the end of the Queue.
            Parameters:
                self -- the current Queue object.
                item -- the item to add to the Queue.
        '''
        self.items.append(item)

    def dequeue(self):
        '''
            Method -- dequeue
                Return and remove the item at the front of the Queue.
            Parameters:
                self -- the current Queue object.
            Returns:
                The item at the front of the Queue
        '''
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def size(self):
        '''
            Method -- size
                Returns the number of items in the Queue.
            Parameters:
                self -- the current Queue object.
            Returns:
                The number of items in the Queue.
        '''
        return len(self.items)
    
    def is_empty(self):
        '''
            Method -- is_empty
                Checks if the Queue is empty.
            Parameters:
                self -- the current Queue object.
            Returns:
                True if the Queue contains no items, False otherwise.
        '''
        return self.size() == 0