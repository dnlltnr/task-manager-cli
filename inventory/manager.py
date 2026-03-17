
from .models import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def _find_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task

    def add_task(self, title):
        if not self.tasks:
            new_id = 1
        else:
            new_id = max(task.id for task in self.tasks) + 1

        new_task = Task(new_id, title)
        self.tasks.append(new_task)

    def delete_task(self, task_id):
        task = self._find_task(task_id)
        if task is None:
            return False
        
        self.tasks.remove(task)
        return True
        
    def list_tasks(self):
        return self.tasks.copy()
    
    def complete_task(self, task_id):
        task = self._find_task(task_id)
        if task is None:
            return False
        
        task.complete()
        return True
