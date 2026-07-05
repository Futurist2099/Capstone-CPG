class Student:
    # Static (class) variable
    school = "Capstone Academy"

    def __init__(self, name, age):
        # Dynamic (instance) variables
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"School: {Student.school}")