class Task:
    def __init__(self, title, priority, completed=False):
        self.title = title
        self.priority = priority
        self.completed = completed
        self.prev = None
        self.next = None
