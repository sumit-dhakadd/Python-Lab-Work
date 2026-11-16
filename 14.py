
import pickle

class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def show(self):
        print("Student Name:", self.name)
        print("Roll No:", self.roll)
        print("Marks:", self.marks)


class PersistenceEngine:

    def __init__(self, filename):
        self.filename = filename

    def store(self, data):
        try:
            with open(self.filename, "wb") as f:
                pickle.dump(data, f)
            print("Data saved successfully!")
        except Exception as e:
            print("Saving Error:", e)

    def restore(self):
        try:
            with open(self.filename, "rb") as f:
                data = pickle.load(f)
            print("Data loaded successfully!")
            return data
        except Exception as e:
            print("Loading Error:", e)
            return None


student_name = input("Enter student name: ")
student_roll = int(input("Enter roll number: "))
student_marks = float(input("Enter marks: "))

obj = Student(student_name, student_roll, student_marks)

engine = PersistenceEngine("student.dat")

engine.store(obj)

new_obj = engine.restore()

if new_obj is not None:
    print("\nRestored Object Details:")
    new_obj.show()
