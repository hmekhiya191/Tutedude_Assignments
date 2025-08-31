#tutedueds Assignmet-2 task-2

# Initial dictionary
students = {
    "Harsh": "A",
    "Payal": "B",
    "Milap": "C"
}

while True:
    print("\n--- Student Grades Menu ---")
    print("1. Add New Student")
    print("2. Update Student Grade")
    print("3. Print All Grades")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        # Add new student
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        if name in students:
            print(f"{name} already exists with grade {students[name]}.")
        else:
            students[name] = grade
            print(f"{name} added successfully.")

    elif choice == 2:
        # Update student grade
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print(f"{name}'s grade updated successfully.")
        else:
            print(f"{name} not found in records.")

    elif choice == 3:
        # Print all grades
        print("\n--- Student Grades ---")
        for name, grade in students.items():
            print(f"{name}: {grade}")

    elif choice == 4:
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
