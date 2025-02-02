from entity import Teacher, Student, Class ,Course, Enrollment
from reports import Reports
from DataBase import Database

def main():
    db = Database()
    
    while True:
        print("\nSchool Management System")
        print("1. Teachers")
        print("2. Students")
        print("3. Courses")
        print("4. Classes")
        print("5. Enrollments")
        print("6. Reports")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("1. Add Teacher")
            print("2. Remove Teacher")
            print("3. Update Teacher")
            print("4. View Teachers")
            sub_choice = input("Enter your choice: ")
            if sub_choice == '1':
                name = input("Enter teacher name: ")
                department = input("Enter department: ")
                Teacher(name, department).add_teacher(db)
            elif sub_choice == '2':
                teacher_id = input("Enter teacher ID: ")
                Teacher.remove_teacher(db, teacher_id)
            elif sub_choice == '3':
                teacher_id = input("Enter teacher ID: ")
                name = input("Enter new name: ")
                department = input("Enter new department: ")
                Teacher.update_teacher(db, teacher_id, name, department)
            elif sub_choice == '4':
                teachers = Teacher.view_teachers(db)
                for teacher in teachers:
                    print(teacher)
        
        elif choice == '2':
            print("1. Add Student")
            print("2. Remove Student")
            print("3. Update Student")
            print("4. View Students")
            sub_choice = input("Enter your choice: ")
            if sub_choice == '1':
                name = input("Enter student name: ")
                email = input("Enter student email: ")
                class_id = int(input("Enter class ID: "))
                Student(name, email, class_id).add_student(db)
            elif sub_choice == '2':
                student_id = input("Enter student ID: ")
                Student.remove_student(db, student_id)
            elif sub_choice == '3':
                student_id = input("Enter student ID: ")
                name = input("Enter new name: ")
                email = input("Enter new email: ")
                class_id = int(input("Enter new class ID: "))
                Student.update_student(db, student_id, name, email, class_id)
            elif sub_choice == '4':
                Student.view_students(db)  

        elif choice == '3':
            print("1. Add Course")
            print("2. View Courses")
            sub_choice = input("Enter your choice: ")
            if sub_choice == '1':
                title = input("Enter course title: ")
                teacher_id = int(input("Enter teacher ID: "))
                Course(title, teacher_id).add_course(db)
            elif sub_choice == '2':
                courses = Course.view_courses(db)
                for course in courses:
                    print(course)

        elif choice == '4':
            print("1. Add Class")
            print("2. View Classes")
            sub_choice = input("Enter your choice: ")
            if sub_choice == '1':
                class_name = input("Enter class name: ")
                Class(class_name).add_class(db)
            elif sub_choice == '2':
                classes = Class.view_classes(db)
                for cls in classes:
                    print(cls)

        elif choice == '5':
            print("1. Enroll Student")
            print("2. Update Grade")
            print("3. View Enrollments")
            sub_choice = input("Enter your choice: ")
            if sub_choice == '1':
                student_id = input("Enter student ID: ")
                course_id = input("Enter course ID: ")
                grade = input("Enter grade (optional): ")
                Enrollment(student_id, course_id, grade).enroll_student(db)
            elif sub_choice == '2':
                enrollment_id = input("Enter enrollment ID: ")
                grade = input("Enter grade: ")
                Enrollment.update_grade(db, enrollment_id, grade)
            elif sub_choice == '3':
                enrollments = Enrollment.view_enrollments(db)
                for enrollment in enrollments:
                    print(enrollment)

        elif choice == '6':
            print("1. Display Enrollment Trends")
            print("2. Analyze Teacher Workload")
            print("3. Summarize Student Performance")
            sub_choice = input("Enter your choice: ")
            if sub_choice == '1':
                Reports.display_enrollment_trends(db)
            elif sub_choice == '2':
                Reports.analyze_teacher_workload(db)
            elif sub_choice == '3':
                student_id = int(input("Enter student ID: "))
                Reports.summarize_student_performance(db, student_id)
        
        elif choice == '7':
            print("Exiting the system.")
            db.close()
            break

if __name__ == "__main__":
    main()
