students = []
def add_student():

    roll = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")
    branch = input("Enter Branch: ")
    marks = float(input("Enter Marks: "))

    student = {
        "roll": roll,
        "name": name,
        "branch": branch,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully.")

def view_students():

    if len(students) == 0:
        print("No student records found.")
        return

    print("\nStudent Records")

    for student in students:

        print("----------------------")
        print("Roll:", student["roll"])
        print("Name:", student["name"])
        print("Branch:", student["branch"])
        print("Marks:", student["marks"])


def search_student():

    roll = input("Enter Roll Number to search: ")

    for student in students:

        if student["roll"] == roll:

            print("Student Found!")
            print("Name:", student["name"])
            print("Branch:", student["branch"])
            print("Marks:", student["marks"])

            return

    print("Student not found.")


def delete_student():

    roll = input("Enter Roll Number to delete: ")

    for student in students:

        if student["roll"] == roll:

            students.remove(student)

            print("Student deleted successfully.")

            return

    print("Student not found.")


def main():

    while True:

        print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


main()