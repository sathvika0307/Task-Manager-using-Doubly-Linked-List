class Task:
    def __init__(self, title, priority, completed=False):
        self.title = title
        self.priority = priority
        self.completed = completed

class Node:
    def __init__(self, task):
        self.task = task
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_task_end(self, task):
        new_node = Node(task)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def add_task_beginning(self, task):
        new_node = Node(task)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete_task(self, title):
        curr = self.head
        while curr:
            if curr.task.title == title:
                if curr.prev:
                    curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                if curr == self.head:
                    self.head = curr.next
                return True
            curr = curr.next
        return False

    def mark_done(self, title):
        curr = self.head
        while curr:
            if curr.task.title == title:
                curr.task.completed = True
                return True
            curr = curr.next
        return False

    def display_tasks(self):
        curr = self.head
        if curr is None:
            print("No tasks to display.")
            return
        print("\nYour Tasks:")
        while curr:
            status = "[x]" if curr.task.completed else "[ ]"
            print(f"{status} {curr.task.title} — Priority: {curr.task.priority}")
            curr = curr.next
