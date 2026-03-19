
# Task Manager CLI

Simple command-line application for managing tasks built in Python.

Built as a learning project focused on:
- Python OOP
- CLI applications
- JSON persistence
- Testing with pytest


## Features

- Add tasks
- Delete tasks
- List tasks
- Mark tasks as completed
- Persistent storage using JSON
- Fully tested with pytest


## Project Structure

task-manager-cli/
│
├── inventory/
│   ├── models.py
│   ├── manager.py
│   ├── cli.py
│
├── tests/
│
├── README.md
├── .gitignore


## Run the app

- Make sure Python is installed

Run in terminal:
```bash
python -m inventory.cli
```

The application creates a `tasks.json` file automatically to store tasks.

## Run tests

Run in terminal:
```bash
python -m pytest
```

## What I Learned

- Designing simple OOP architecture
- Separating concerns (CLI vs Business logic)
- Working with JSON
- Writing simple tests using pytest
- Handling file-based persistence


## Future Improvements

- Edit task title
- Add due dates
- Add task priorities
- Improve CLI UX
