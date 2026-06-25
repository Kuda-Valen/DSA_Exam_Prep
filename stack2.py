from collections import deque

class Stack:
    def __init__(self):
        self.collection = deque()
    
    def push(self, item):
        self.collection.append(item)
    
    def pop(self):
        if not self.collection:
            print("Nothing to pop")
        
        else:
            return self.collection.pop()
    
    def peek(self):
        if not self.collection:
            print("Nothing in collection")
        
        else:
            return self.collection[-1]
    
    def is_empty(self):
        if not self.collection:
            return True
        else:
            return False
    
    def size(self):
        size = len(self.collection)
        return size

if __name__ == "__main__":
    collection = Stack()

    while True:
        print("\n1. Add Item to Stack")
        print("2. Remove top item")
        print("3. Peek top item")
        print("4. Check if Stack is Empty")
        print("5. Check stack size")
        print("6. Exit..")

        try:
            option = int(input("\nChoose an option: "))

            if option == 1:
                item = input("\nEnter item to append: ")
                collection.push(item)
                print("Successfully add item!\n")
            
            elif option == 2:
                popped = collection.pop()
                print(f"\nSuccessfully removed item: {popped}")

            elif option == 3:
                item = collection.peek()
                print(f"\nNext Item on top of Stack: {item}")
            
            elif option == 4:
                boolean = collection.is_empty()

                if boolean == True:
                    print("\nStack is empty!")
                
                else:
                    print("\nStack is not empty")

            elif option == 5:
                size = collection.size()
                print(f"\nThe size of Stack is: {size}")
            
            elif option == 6:
                print("\nExiting..")
                break

            else:
                print("\nInvalid option! Choose a valid option..")

        except ValueError as e:
            print(f"\nInvalid Input!! Error: {e}")