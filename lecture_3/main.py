def main():
    """Handles user interaction and menu navigation for the Student Grade Analyzer"""
    students = []
    while True:
        print("----- Student Grade Analyzer -----\n"
              "1. Add a new student\n"
              "2. Add grades for a student\n"
              "3. Generate a full report\n"
              "4. Find the top student\n"
              "5. Exit program\n")
        while True:
            try:
                choice = int(input("Enter your choice: "))
                break
            except ValueError:
                print("Invalid input, please enter a number")
        if choice == 1:
            add_student(students)
        elif choice == 2:
            add_grades(students)
        elif choice == 3:
            show_report(students)
        elif choice == 4:
            find_top_student(students)
        elif choice == 5:
            break
        else:
            print("This option doesn't exist :(")

def add_student(students: list) -> None:
    """Add a new student to the students list"""
    while True:
        student_name = input("Enter student name: ").strip()
        if not valid_string(student_name):
            print("Invalid input, please enter a valid student name")
            continue
        if any(student_name == student["name"] for student in students):
                print("Student name is already taken")
                break
        students.append({"name": student_name, "grades": []})
        break

def add_grades(students: list) -> None:
    """Add grades to a student"""
    while True:
        student_name = input("Enter student name: ").strip()
        if not valid_string(student_name):
            print("Invalid input, please enter a valid student name")
            continue
        student = None
        for s in students:
            if s["name"] == student_name:
                student = s
                break
        if student is None:
            print("Student not found")
            break

        while True:
            student_grade = input("Enter student grade(enter 'done' to stop): ")
            if student_grade.lower() == "done":
                break
            try:
                student_grade = int(student_grade)
                if not (0 <= student_grade <= 100):
                    print("Invalid grade, please enter a valid grade(0 - 100)")
                    continue
            except ValueError:
                print("Invalid input, please enter a grade(number)")
                continue
            student["grades"].append(student_grade)
        break

def show_report(students: list) -> None:
    """Print a report of all students"""
    print("----- Student Report -----")
    if not students:
        print("There are no students")
        return
    students_with_grades = 0
    sum_average_grades = 0
    max_average = 0
    min_average = 100
    for student in students:
        average_grade = sum(student['grades'])/len(student['grades']) if student['grades'] else 'N/A'
        print(f"{student['name']}'s average grade is {average_grade}")
        if average_grade == 'N/A':
            continue
        students_with_grades += 1
        sum_average_grades += average_grade
        if average_grade > max_average:
            max_average = average_grade
        if average_grade < min_average:
            min_average = average_grade
    if students_with_grades == 0:
        print("No student has any grades yet")
        return
    print(f"-------------------------------\n"
          f"Max Average: {max_average:.1f}\n"
          f"Min Average: {min_average:.1f}\n"
          f"Overall Average: {(sum_average_grades / students_with_grades):.1f}\n"
          f"-------------------------------")

def find_top_student(students: list) -> None:
    """Find the top student"""
    if not students:
        print("There are no students")
        return
    students_with_grades = [student for student in students if student["grades"]]
    if len(students_with_grades) == 0:
        print("No student has any grades yet")
        return
    # find the student with the highest average grade
    top_student = max(students_with_grades, key = lambda student: sum(student["grades"])/len(student["grades"]))
    print(f"The student with the highest average is {top_student['name']} with a grade of {(sum(top_student['grades'])/len(top_student['grades'])):.1f}")

def valid_string(s: str) -> bool:
    """Check if string is valid"""
    if not s or s.isdigit():
        return False
    return True

if __name__ == "__main__":
    main()