
class Task:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.completed = False

    def __repr__(self):
        return f"id={self.id}, title={self.title}, completed={self.completed}"
    
    def complete(self):
        self.completed = True

    