# Learn Python — Coding Studio

A small collection of learning materials, example scripts, and Jupyter notebooks used for Python lessons and hands-on exercises.

**Project layout (root)**

- `exercise5.ipynb` — Notebook: student grades example and sorting exercises.
- `sesi-1.ipynb`, `sesi-3.ipynb`, `session5.ipynb` — Teaching notebooks covering basics: print, control flow, data structures, functions, and sorting (bubble sort).
- `sesi-2_exercise.py` — Small Python script with variables, types, loops, and conditional examples.
- `helllo.py` — Tiny demo script that prints a greeting.
- `sesi-6/` — Folder for session 6 materials (notebooks and text files may be inside).
- `sesi-7/` — GUI examples using `tkinter`:
  - `button.py`, `entry.py`, `error_handling.py`, `grid.py`, `label.py`, `pack.py`, `place.py`
- `test.html` — Simple example HTML file.
- `random.txt`, `test.txt` — Not present in the repository (placeholders referenced during inspection).

## About

This workspace is intended for students learning Python basics and simple GUI programming with `tkinter`. Files are organized by session (`sesi-*`) and contain short, focused examples that are easy to run and modify.

## How to run the Python scripts (Windows PowerShell)

Open PowerShell in the project folder (`c:\Users\Lenovo\Documents\learning python`) and run:

```powershell
python helllo.py
python sesi-2_exercise.py
python sesi-7\button.py    # runs a tkinter demo (requires a GUI environment)
```

Notes:

- Notebooks (`.ipynb`) can be opened with VS Code's Jupyter support or in Jupyter Notebook / JupyterLab.
- `tkinter` is included with standard CPython installs on Windows. If a `tkinter` import fails, ensure Python was installed with the tcl/tk option.

## Quick file descriptions

- `helllo.py`: Prints "Hello world!" — quick sanity check for Python execution.
- `sesi-2_exercise.py`: Demonstrates variables, types, formatted strings, conditionals, `for` and `while` loops.
- `session5.ipynb` / `exercise5.ipynb`: Show bubble sort implementations and a small console demo (sorting products by price/name).
- `sesi-7/*`: Several small `tkinter` examples demonstrating layout managers (`pack`, `grid`, `place`), widgets (`Label`, `Entry`, `Button`), and simple error handling with dialog boxes.
### 