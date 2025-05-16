# Student Management System

A simple Flask-based student management system with CRUD operations.

## Project Structure

```
student_management_system/
├── app.py
├── static/
│   └── styles.css
├── templates/
│   ├── index.html
│   ├── add.html
│   └── edit.html
└── students.db (created automatically)
```

## Features

- Create, read, update, and delete student records
- SQLAlchemy ORM for database operations
- Clean and responsive UI

## Installation

1. Clone the repository or download the files
2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies

```bash
pip install flask flask-sqlalchemy
```

4. Run the application

```bash
python app.py
```

5. Open your browser and navigate to `http://localhost:5000`

## Database Schema

The application uses SQLite with the following schema:

- **Student**
  - id (Integer, Primary Key)
  - name (String)
  - age (Integer)
  - grade (String)

## Usage

The application provides a web interface for managing students:

- View all students on the homepage
- Add new students using the "Add New Student" button
- Edit existing students by clicking the "Edit" button
- Delete students by clicking the "Delete" button

Additionally, the CRUD operations can be used programmatically:

```python
# Add a student
add_student("John Doe", 18, "12th")

# Get a student by ID
student = get_student_by_id(1)

# Get all students
students = get_all_students()

# Update a student
update_student(1, "John Doe Updated", 19, "12th")

# Delete a student
delete_student(1)
```
