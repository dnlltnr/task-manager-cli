
from .manager import TaskManager

def menu():
    print()
    print("1 - Add task")
    print("2 - Delete task")
    print("3 - List task")
    print("4 - Complete task")
    print("5 - Exit")
    print()


def add_task_action(task_manager):
    title = input("Write a title for your task:\n")
    task_manager.add_task(title)


def delete_task_action(task_manager):
    task_id = int(input("Which task do you wish to delete?\n"))
    task_manager.delete_task(task_id)


def list_task_action(task_manager):
    tasks = task_manager.list_tasks()
    if not tasks:
            print("\nNo tasks found.\n")
            return
    
    for task in tasks:
        status = "✔" if task.completed else "❌"
        print(f"{task.id} | {task.title} | {status}")


def complete_task_action(task_manager):
    task_id = int(input("Which task do you wish to mark as completed?\n"))
    task_manager.complete_task(task_id)


ACTIONS = {
    "1": add_task_action,
    "2": delete_task_action,
    "3": list_task_action,
    "4": complete_task_action
}


def handle_choice(choice, task_manager):
    action = ACTIONS.get(choice)
    if action:
        action(task_manager)
    else:
        print("\nInvalid choice.")


def main():
    task_manager = TaskManager()

    while True:
        menu()
        choice = input("Choose an option: ")
        if choice == "5":
            print("Exiting the aplication...")
            break
        handle_choice(choice, task_manager)

if __name__ == "__main__":
    main()

