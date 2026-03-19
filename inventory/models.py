
class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    def __repr__(self):
        return f"id={self.id}, title={self.title}, completed={self.completed}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["title"], data["completed"])

    def complete(self):
        self.completed = True

    