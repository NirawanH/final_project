# Task management Board

This is a task management board written in Python. You can create task lists (like "To Do", "In Progress", "Done") and add/edit/move cards within those lists — similar to Trello, but entirely in your terminal.

---

## Features

- Add, edit, and delete task lists
- Add, edit, move, and delete cards
- Set deadlines for each card
- Save and load board data using JSON
- Clean terminal display using `tabulate`
- Includes unit tests for all core features

---

## Requirements

Make sure you have Python 3.10+ installed.  
Then install the required packages using:

```bash
pip install -r requirements.txt
```

> Tip: It’s recommended to use a virtual environment.

```bash
# Create and activate a virtual environment (optional)
python -m venv myenv
# Windows
.\myenv\Scripts ctivate
# macOS/Linux
source myenv/bin/activate
```

---

## How to Run

```bash
python main.py
```

This will launch the interactive menu in your terminal.

---

## 📁 Project Structure

```
myenvironment/
├── requirements.txt
├── board_data.json           # Automatically saved state
├── README.md
├── src/
│   ├── Board.py
│   ├── Card.py
│   └── main.py
│   └── TaskList.py
├── tests/
│   ├── test_Board.py
│   ├── test_Card.py
│   └── test_TaskList.py
```

---

## Running Tests

Tests are written using `pytest`.

```bash
pytest
```

---

## Notes

- Uses JSON for data persistence (`board_data.json`)
- `tabulate` is used to format board/card tables
- Project is organized using object-oriented design



