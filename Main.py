class Solution:
    """This class implements linear queue.
      Attributes:
          stack: A list which maintains the content of stack.
          queue: A list which maintains the content of queue.
          top: An integer which denotes the index of the element at the top of the stack.
          front: An integer which denotes the index of the element at the front of the queue.
          rear: An integer which denotes the index of the element at the rear of the queue.
          size: An integer which represents the size of stack and queue.
      """

    # Write your code here
    def __init__(self, size):
        """Inits Solution with stack, queue, size, top, front and rear.
        Arguments:
          size: An integer to set the size of stack and queue.
        """
        self.stack = []
        self.queue = []
        self.size = size
        self.top = -1
        self.rear = -1
        self.front = -1

    def is_stack_empty(self):
        """
        Check whether the stack is empty.
        Returns:
          True if it is empty, else returns False.
        """
        if (len(self.stack) == 0):
            return True
        else:
            return False

    def is_queue_empty(self):
        """
        Check whether the queue is empty.
        Returns:
          True if it is empty, else returns False.
        """
        if (len(self.queue) == 0):
            return True
        else:
            return False

    def is_stack_full(self):
        """
        Check whether the stack is full.
        Returns:
          True if it is full, else returns False.
        """
        if (self.top == self.size):
            return True
        else:
            return False

    def is_queue_full(self):
        """
        Check whether the queue is full.
        Returns:
          True if it is full, else returns False.
        """
        if (self.rear == self.size - 1):
            return True
        else:
            return False

    def push_character(self, character):
        """
        Push the character to stack, if stack is not full.
        Arguments:
            character: A character that will be pushed to the stack.
        """
        if (not self.is_stack_full()):
            self.stack.append(character)
            self.top += 1
        else:
            print("Stack is full")


def enqueue_character(self, character):
    """
    Enqueue the character to queue, if queue is not full.
    Arguments:
        character: A character that will be enqueued to queue.
    """
    if (not self.is_queue_full()):
        if (self.front == -1):
            self.front = 0
            self.rear += 1
            self.queue.append(character)
        else:
            print("Queue is full")


def pop_character(self):
    """
    Do pop operation if the stack is not empty.
    Returns:
      The data that is popped out if the stack is not empty.
    """
    if (not self.is_stack_empty()):
        self.stack.pop()
        self.top -= 1
    else:
        print("Stack is full")


def dequeue_character(self):
    """
    Do dequeue operation if the queue is not empty.
    Returns:
      The data that is dequeued if the queue is not empty.
    """
    if (not self.is_queue_empty()):
        self.queue.pop(self.front)
    else:
        print("queue is empty")


# read the string text
text = input()

# find the length of text
length_of_text = len(text)

# Create the Solution class object
solution = Solution(length_of_text)

# push/enqueue all the characters of string text to stack
for index in range(length_of_text):
    val = text[index]
    solution.push_character(val)
    solution.enqueue_character(val)

is_palindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both characters
If the comparison fails, set is_palindrome as False.
'''
for i in range(length_of_text):
    stack_pop, queue_pop = solution.pop_character(), solution.dequeue_character()
    if (stack_pop == queue_pop):
        is_palindrome = True
    else:
        is_palindrome = False

# finally print whether string text is palindrome or not.
if is_palindrome:
    print("The word, " + text + ", is a palindrome.")
else:
    print("The word, " + text + ", is not a palindrome.")
