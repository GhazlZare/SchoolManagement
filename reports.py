import pandas as pd
import matplotlib.pyplot as plt
from DataBase import Database

class Reports:
    @staticmethod
    def display_enrollment_trends(db):
        """Visualize enrollment trends over time"""
        query = "SELECT course_id, COUNT(student_id) FROM enrollments GROUP BY course_id"
        data = db.fetch_results(query)
        
        df = pd.DataFrame(data, columns=['Course ID', 'Enrollment Count'])
        df['Enrollment Count'] = pd.to_numeric(df['Enrollment Count'], errors='coerce')
        df = df.dropna(subset=['Enrollment Count'])
        
        if not df.empty:
            df.plot(x='Course ID', y='Enrollment Count', kind='line', marker='o')
            plt.title("Enrollment Trends")
            plt.xlabel("Course ID")
            plt.ylabel("Number of Enrollments")
            plt.show()
        else:
            print("No data available for enrollment trends.")

    
    @staticmethod
    def summarize_student_performance(db, student_id):
        """Visualize student performance across courses"""
        query = "SELECT course_id, grade FROM enrollments WHERE student_id = %s"
        data = db.fetch_results(query, (student_id,))
        
        if not data:  
            print(f"No performance data found for student ID {student_id}.")
            return

        df = pd.DataFrame(data, columns=['Course ID', 'Grade'])
        df['Grade'] = pd.to_numeric(df['Grade'], errors='coerce')
        df.dropna(subset=['Grade'], inplace=True)

        if df.empty:
            print(f"No valid numeric grade data for student ID {student_id}.")
            return

        df.plot(x='Course ID', y='Grade', kind='line', marker='o')
        plt.title(f"Student {student_id} Performance")
        plt.xlabel("Course ID")
        plt.ylabel("Grade")
        plt.show()

    @staticmethod
    def analyze_teacher_workload(db):
        """Analyze teacher workload"""
        query = "SELECT teacher_id, COUNT(course_id) FROM courses GROUP BY teacher_id"
        data = db.fetch_results(query)
        df = pd.DataFrame(data, columns=['Teacher ID', 'Courses Taught'])
        if not df.empty:
            df.plot(x='Teacher ID', y='Courses Taught', kind='bar')
            plt.title("Teacher Workload Analysis")
            plt.xlabel("Teacher ID")
            plt.ylabel("Number of Courses")
            plt.show()
        else:
            print("No data available for teacher workload analysis.")