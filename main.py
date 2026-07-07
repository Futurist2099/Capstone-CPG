from student import Student

# Create student objects
student1 = Student("Kiesha", 25)
student2 = Student("Tyrone", 22)

# Display information
student1.display_info()
print()

student2.display_info()

print("\nChanging the static variable...\n")

# Change static variable
Student.school = "Capstone Academy"

student1.display_info()
print()

student2.display_info()