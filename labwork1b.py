students=[]
courses=[]
marks={}


def input_number_students():
    return int(input("Enter number of students: "))

# student info
def student_info(number_students):
    for i in range(number_students):
        student_name=input("Enter student name: ")
        id=int(input("Enter student ID: "))
        dob=input("Enter student date of birth: ")
        students.append({"name": name, "id": id, "dob": dob})

def input_number_course():
    return int(input("Enter number of courses: "))

#course info
def course_info(num_courses):
    for i in range(num_courses):
        course_name=input("Enter course name: ")
        course_id=int(input("Enter course ID: "))
        courses.append({"name": course_name, "id": course_id})

def students():
    print("---list of students---")
    for student in students:
        print(f"ID: {student['id']}, name: {student['name']}, date of birth: {student['dob']}")

def courses():
    print("---list of courses---")
    for course in courses:
        print(f"ID: {course['id']}, name: {course['name']}")

def input_marks():
    input_course=input("Enter ID course to enter marks: ")
    marks[input_course]={}
    for student in students:
        mark=float(input(f"Enter mark for {student['name']}: "))
        marks[input_course][student['id']]=mark

def marks(student_name):
    print("---list of marks---")
    course_id=input("Enter course ID to view marks: ")
    if course_id in marks:
        for student_id, mark in marks[course_id].items():
            print(f"Student: {student_name} ==> Mark: {mark}")
    else:
        print("No marks found for the specified course.")

def main():
    number_students=input_number_students()
    student_info(number_students)
    number_course=input_number_course()
    course_info(number_course)

    students()
    courses()

    input_marks()
    marks()

if __name__=="__main__":
    main()







