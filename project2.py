def grade_calculator():

    name = input("Enter student name: ")

    math = float(input("Enter Math marks: "))
    python = float(input("Enter Python marks: "))
    english = float(input("Enter English marks: "))

    total = math + python + english

    maximum_marks = 300

    percentage = (total / maximum_marks) * 100

    print("\nStudent Name:", name)
    print("Total Marks:", total)
    print("Maximum Marks:", maximum_marks)
    print("Percentage:", percentage)

    if percentage >= 90:
        print("Grade: A")

    elif percentage >= 75:
        print("Grade: B")

    elif percentage >= 60:
        print("Grade: C")

    elif percentage >= 40:
        print("Grade: D")

    else:
        print("Grade: F")


grade_calculator()