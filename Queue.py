from collections import deque

class Queue:
    def __init__(self):
        self._queue = deque()

    def enqueue(self, item):
        self._queue.append(item)
        
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue Underflow: Cannot dequeue from an empty queue.")
        return self._queue.popleft()
        
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue Underflow: Cannot dequeue from an empty queue.")
        return self._queue[0]
    
    def peek_last(self):
        if self.is_empty():
            raise IndexError("Queue Underflow: Cannot dequeue from an empty queue.")
        return self._queue[-1]
        
    def is_empty(self):
        return len(self._queue) == 0
    
    def size(self):
        return len(self._queue)

if __name__ == "__main__":
    queue = Queue()

    while True:
        print("\n1. Add item to your Queue")
        print("2. See item first in the Queue")
        print("3. See item last in the Queue")
        print("4. Remove item first in the Queue")
        print("5. Check if Queue is empty")
        print("6. Check size of the Queue")
        print("7. Exit..")

        try:
            option = int(input("Choose an option: "))

            if option == 1:
                item = input("\nEnter item to add: ")
                queue.enqueue(item)
            
            elif option == 2:
                item = queue.peek()
                print(f"\nItem first in Queue is: '{item}'")
            
            elif option == 3:
                item = queue.peek_last()
                print(f"\nItem last in Queue is: '{item}'")
            
            elif option == 4:
                item = queue.dequeue()
                print(f"\nItem '{item}' has been removed successfully..")
            
            elif option == 5:
                boolean = queue.is_empty()
                if boolean == False:
                    print("\nQueue is not empty.")
                else:
                    print("\nQueue is empty.")
            
            elif option == 6:
                size = queue.size()
                print(f"\nThe size of the Queue is: {size}")
            
            elif option == 7:
                print("\nExiting...")
                break
            
            else:
                print("Invalid option. Choose valid option!!!!")

        except ValueError:
            print("Invalid Input. Enter valid input!!!!")