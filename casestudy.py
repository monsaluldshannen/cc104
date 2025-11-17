students = []

def add_student():
    sid = input("Enter ID: ")   # any type allowed (string)
    name = input("Enter name: ")

    grade_input = input("Enter grade: ")
    try:
        grade = float(grade_input)
    except ValueError:
        grade = grade_input  # allow any type

    student = {"id": sid, "name": name, "grade": grade}
    students.append(student)
    print("Student added successfully!")


def bubble_sort_by_name():
    n = len(students)
    for i in range(n):
        for j in range(0, n - i - 1):
            if students[j]["name"] > students[j + 1]["name"]:
                students[j], students[j + 1] = students[j + 1], students[j]


def bubble_sort_by_id():
    n = len(students)
    for i in range(n):
        for j in range(0, n - i - 1):
            if str(students[j]["id"]) > str(students[j + 1]["id"]):
                students[j], students[j + 1] = students[j + 1], students[j]


def binary_search_by_id(target_id):
    bubble_sort_by_id()  # MUST sort first
    target_id = str(target_id)

    left, right = 0, len(students) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_id = str(students[mid]["id"])

        if mid_id == target_id:
            return students[mid]
        elif mid_id < target_id:
            left = mid + 1
        else:
            right = mid - 1
    return None


# ------------------------------
#   PROGRAM MENU (fixes issue)
# ------------------------------

while True:
    print("\n===== STUDENT SYSTEM =====")
    print("1. Add student")
    print("2. Search student by ID")
    print("3. Sort students by name")
    print("4. Show all students")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        tid = input("Enter ID to search: ")
        result = binary_search_by_id(tid)
        if result:
            print("Student found:", result)
        else:
            print("Student not found.")

    elif choice == "3":
        bubble_sort_by_name()
        print("Students sorted by name!")

    elif choice == "4":
        print("\n--- STUDENT LIST ---")
        for s in students:
            print(s)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option")
