"""The Challenge: The catch is that finding the minimum value in a standard stack 
typically takes O(n) time because you would have to search the whole stack. To achieve 
O(1) time for getMin(), you have to figure out how to maintain a running record of the
 minimum without sacrificing the Last-In-First-Out (LIFO) integrity of your stack."""

"""Pro-Tip for the Implementation: Instead of relying on built-in Python lists that expose 
all list methods (like .insert() or .sort() which can corrupt stack integrity), build your 
custom class from scratch using either an encapsulated list or a linked-node structure, and 
optimize your getMin() using an auxiliary (helper) stack"""

from collections import deque

class DequeStack:
    def __init__(self):
        self.stack = deque()
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.stack:
            raise IndexError("Pop from an empty stack")
        return self.stack.pop()
    
    def peek(self):
        if self.stack:
            return self.stack[-1]
        
        else: 
            None

if __name__ == "__main__":
    stack = DequeStack()

    print("\nTesting Stacks..\n")

    while True: 
        print("1. Add Name to the Stack")
        print("2. Remove name from stack")
        print("3. See which name is on top of stack")
        print("5. Exit")

        try:
            option = int(input("\nChoose an option: "))

            if option == 1: 
                name = input("\nEnter name to add: ")
                stack.push(name)
                print("Name added successfully!!")
            
            elif option == 2:
                poped = stack.pop()
                print(f"\nSuccessfully popped :{poped}")
            
            elif option == 3:
                item = stack.peek()
                print(f"\nThe next item on top is: {item}")
            
            elif option == 5:
                print("Exiting...")
                break
            
            else:
                print("Invalid option! Choose a valid option")

        except ValueError as e:
            print(f"Invalid input!! Error: {e}")