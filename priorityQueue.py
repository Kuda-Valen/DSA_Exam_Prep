import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority ,item))
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty queue")
        return heapq.heappop(self._queue)[1] 
    
    def peek(self):
        if self.is_empty():
            raise IndexError("pop from an empty queue")
        return self._queue[1]
    
    def is_empty(self):
        return len(self._queue) == 0
    
    def size(self):
        return len(self._queue)
    
if __name__ == "__main__":
    priority_queue = PriorityQueue()

    while True:
        print("\n1. Push new item")
        print("2. Pop item")
        print("3. Peek Item")
        print("4. See number of items")
        print("5. Exit")

        try:
            option = int(input("\nChoose an Option: "))

            if option == 1:
                name = input("\nEnter item name: ")
                priority = int(input("Enter the priority (1-5): "))

                priority_queue.push(priority, name)
                print(f"Item: {name} has been pushed successfully..")

            elif option == 2:
                item = priority_queue.pop()
                print(f"Successfully popped: {item}")

            elif option == 3:
                item = priority_queue.peek()
                print(f"Item to peek: {item}")

            elif option == 4:
                size = priority_queue.size()
                print(f"Size of the Priority Queue: {size}")
            
            elif option == 5:
                print("Exiting..")
                break

            else:
                print("Invalid option. Choose a valid option!!!")

        except ValueError:
            print("Invalid input. Choose valid input")