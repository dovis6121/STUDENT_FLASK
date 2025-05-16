from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from typing import List, Optional

app: Flask = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']: str = 'sqlite:///students.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db: SQLAlchemy = SQLAlchemy(app)

class Student(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), nullable=False)
    age: int = db.Column(db.Integer, nullable=False)
    year: str = db.Column(db.String(10), nullable=False)

    def __repr__(self) -> str:
        return f"<Student {self.name}>"

with app.app_context():
    db.create_all()


def add_student(name: str, age: int, year: str) -> None:
    new_student = Student(name=name, age=age, year=year)
    db.session.add(new_student)
    db.session.commit()

def get_student_by_id(id: int) -> Optional[Student]:
    return Student.query.get(id)

def get_all_students() -> List[Student]:
    return Student.query.all()

def update_student(id: int, name: str, age: int, year: str) -> None:
    student = Student.query.get(id)
    if student:
        student.name = name
        student.age = age
        student.year = year
        db.session.commit()

def delete_student(id: int) -> None:
    student = Student.query.get(id)
    if student:
        db.session.delete(student)
        db.session.commit()

# Routes for web interface
@app.route('/')
def index():
    students = get_all_students()
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        year = request.form['year']
        add_student(name, age, year)
        flash('Student added successfully!')
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    student = get_student_by_id(id)
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        year = request.form['year']
        update_student(id, name, age, year)
        flash('Student updated successfully!')
        return redirect(url_for('index'))
    return render_template('edit.html', student=student)

@app.route('/delete/<int:id>')
def delete(id):
    delete_student(id)
    flash('Student deleted successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        add_student("John Doe", 18, "12th")
        add_student("Jane Smith", 17, "11th")
        add_student("Bob Johnson", 16, "10th")

        student = get_student_by_id(1)
        if student:
            print(f"Found student: {student.name}, age: {student.age}, year: {student.year}")

        all_students = get_all_students()
        print("All students:")
        for student in all_students:
            print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}, year: {student.year}")

        update_student(1, "John Doe Updated", 19, "12th")
        updated_student = get_student_by_id(1)
        if updated_student:
            print(f"Updated student: {updated_student.name}, age: {updated_student.age}, year: {updated_student.year}")

        delete_student(3)
        remaining_students = get_all_students()
        print("Remaining students after deletion:")
        for student in remaining_students:
            print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}, year: {student.year}")
    
    app.run(debug=True)