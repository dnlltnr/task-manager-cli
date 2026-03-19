
from inventory.manager import TaskManager

def test_add_task():
    manager = TaskManager()
    manager.tasks = []

    manager.add_task("walk")

    assert len(manager.tasks) == 1
    assert manager.tasks[0].id == 1
    assert manager.tasks[0].title == "walk"


def test_delete_task():
    manager = TaskManager()
    manager.tasks = []

    manager.add_task("walk")
    manager.add_task("run")
    result = manager.delete_task(1)

    assert len(manager.tasks) == 1
    assert manager.tasks[0].title == "run"
    assert manager.tasks[0].id == 2
    assert result == True


def test_complete_task():
    manager = TaskManager()
    manager.tasks = []

    manager.add_task("walk")
    result = manager.complete_task(1)

    assert manager.tasks[0].completed == True
    assert result == True


def test_save_and_load_tasks(tmp_path):
    file_path = tmp_path / "tasks.json"

    manager = TaskManager(file_path)
    manager.tasks = []

    manager.add_task("walk")
    manager.save_tasks()

    new_manager = TaskManager(file_path)

    assert len(new_manager.tasks) == 1
    assert new_manager.tasks[0].title == "walk"
    
