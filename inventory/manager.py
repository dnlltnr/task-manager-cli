
from .models import Task
import json

class TaskManager:
    def __init__(self, file_path="tasks.json"):
        self.file_path = file_path
        self.tasks = []
        self.load_tasks()

    def save_tasks(self):
        tasks_data = [task.to_dict() for task in self.tasks]

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(tasks_data, file, indent=4)

    def load_tasks(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            self.tasks = []
            return
        
        self.tasks = []
        for task_data in data:
            task = Task.from_dict(task_data)
            self.tasks.append(task)


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
        self.save_tasks()

    def delete_task(self, task_id):
        task = self._find_task(task_id)
        if task is None:
            return False
        
        self.tasks.remove(task)
        self.save_tasks()
        return True
        
    def list_tasks(self):
        return self.tasks.copy()
    
    def complete_task(self, task_id):
        task = self._find_task(task_id)
        if task is None:
            return False
        
        task.complete()
        self.save_tasks()
        return True
