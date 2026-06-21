# UnProf_Pyai_1

# Student Report Card System

A Python console application built as part of a Python & AI internship at unprof task (Day 1 – OOP: Classes & Objects).

## Features

- Add student details (name, roll number)
- Add or update subject grades
- Display a formatted report card with average marks and an overall letter grade
- Supports honors students with scholarship info via inheritance

## OOP Concepts Demonstrated

- **Classes & Objects** – `Student` is the base class; objects are created from it via the interactive menu
- **`__init__` constructor** – initializes name, roll number, and an empty grades dictionary
- **Methods** – `add_grade()`, `update_grade()`, `calculate_average()`, `display_report_card()`
- **Inheritance** – `HonorsStudent` extends `Student` using `super()`, adding scholarship details on top of the base functionality

## How to Run

```bash
python3 report-card.py
```

Follow the on-screen menu to add a student, add/update grades, and view the report card.

## Project Structure

```
.
├── report-card.py
└── README.md
```
