
from inventory.models import Task


def test_task_creation():
    task = Task(1, "walk")

    assert task.id == 1
    assert task.title == "walk"
    assert task.completed == False


def test_task_complete():
    task = Task(1, "walk")

    task.complete()

    assert task.completed == True


def test_task_to_dict():
    task = Task(1, "walk", True)
    result = task.to_dict()

    assert result == {
        "id": 1,
        "title": "walk",
        "completed": True
    }


def test_task_from_dict():
    data = {
        "id": 1,
        "title": "walk",
        "completed": True
    }

    task = Task.from_dict(data)

    assert task.id == 1
    assert task.title == "walk"
    assert task.completed == True
