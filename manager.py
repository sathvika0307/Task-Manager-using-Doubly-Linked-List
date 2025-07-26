from doubly_linked_list import DoublyLinkedList, Task

def main():
    dll = DoublyLinkedList()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task (End)")
        print("2. Add Task (Beginning)")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Show All Tasks")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            t = input("Title: ")
            p = input("Priority (High/Medium/Low): ")
            task = Task(t, p)
            dll.add_task_end(task)

        elif choice == '2':
            t = input("Title: ")
            p = input("Priority (High/Medium/Low): ")
            task = Task(t, p)
            dll.add_task_beginning(task)

        elif choice == '3':
            t = input("Title to delete: ")
            if dll.delete_task(t):
                print("Deleted.")
            else:
                print("Task not found.")

        elif choice == '4':
            t = input("Title to mark as done: ")
            if dll.mark_done(t):
                print("Marked as done.")
            else:
                print("Task not found.")

        elif choice == '5':
            dll.display_tasks()

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
