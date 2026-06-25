"""Interactive System to send tasks to a remote robot"""

from datetime import datetime
from collections import deque

class Task:
    def __init__(self, name: str, time: datetime, details: str):
        self.name = name 
        self.time = time
        self.details = details
    
class Tasks:
    def __init__(self):
        self._tasks = deque()
    
    def enqueue(self):
        name = input("Enter Tasks Name: ")
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        details = input("Enter details of the Task: ")

        task = Task(name, time, details)
        self._tasks.append(task)
        print(f"Task '{name}' has been added successfully.")
    
    def dequeue(self):
        if not self._tasks:
            raise IndexError("There are no tasks in queue")
        return self._tasks.popleft()
    
    def peek_left(self):
        if not self._tasks:
            raise IndexError("There are no tasks in queue")
        return self._tasks[0]
    
    def peek_right(self):
        if not self._tasks:
            raise IndexError("There are no tasks in queue")
        return self._tasks[-1]
    
    def size(self):
        return len(self._tasks)
    
if __name__ == "__main__":
    tasks = Tasks()

    while True:
        print("\n== Robot Tasks System ==\n")
        print("1. Add Task")
        print("2. View Task first in Queue")
        print("3. View Tasks last in Queue")
        print("4. Execute Task first in Queue")
        print("5. See Number of Total Tasks in Queue")
        print("6. Exit..")

        try:
            option = int(input("\nChoose an option: "))

            if option == 1:
                tasks.enqueue()

            elif option == 2:
                task = tasks.peek_left()
                print(f"\nThe task next in Queue is: {task.name} | {task.time} | {task.details}")

            elif option == 3:
                task = tasks.peek_right()
                print(f"\nThe task last in Queue is: {task.name}")
            
            elif option == 4:
                task = tasks.dequeue()
                current_time = datetime.now().strftime("%H:%M:%S")
                print(f"\nSuccessfully executed{task.name} at {current_time}")

            elif option == 5:
                size = tasks.size()
                print(f"\nTotal Tasks in Queue are: {size}")

            elif option == 6:
                print("\nExiting...")
                break
            
            else:
                print("Invalid option. Choose a Valid Option!!!")
        except ValueError:
            print("Invalid input. Enter Valid input!")

