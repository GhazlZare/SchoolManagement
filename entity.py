# models.py
from DataBase import Database
import logging

class Teacher:
    def __init__(self, name, department):
        self.name = name
        self.department = department
    
    def add_teacher(self, db):
        """Add teacher to database"""
        pass
    
    @staticmethod
    def remove_teacher(db, teacher_id):
        """Remove teacher from database"""
        pass
    
    @staticmethod
    def update_teacher(db, teacher_id, new_name=None, new_department=None):
        """Edit teacher details"""
        pass
    
    @staticmethod
    def view_teachers(db):
        """Fetch all teachers"""
        pass

class Student:
    def __init__(self, name, email, class_id):
        self.name = name
        self.email = email
        self.class_id = class_id
    
    def add_student(self, db):
        """Add student to database with class_id validation"""
        pass
    
    @staticmethod
    def remove_student(db, student_id):
        """Remove student from database"""
        pass
    
    @staticmethod
    def update_student(db, student_id, new_name=None, new_email=None, new_class_id=None):
        """Edit student details"""
        pass
    
    @staticmethod
    def view_students(db):
        """Fetch all students"""
        pass


class Course:
    def __init__(self, title, teacher_id):
        self.title = title
        self.teacher_id = teacher_id
    
    def add_course(self, db):
        """Add course to database"""
        pass

    
    @staticmethod
    def view_courses(db):
        """Fetch all courses"""
        pass

class Class:
    def __init__(self, class_name):
        self.class_name = class_name
    
    def add_class(self, db):
        """Add class to database"""
        pass

    
    @staticmethod
    def view_classes(db):
        """Fetch all classes"""
        pass

class Enrollment:
    def __init__(self, student_id, course_id, grade=None):
        self.student_id = student_id
        self.course_id = course_id
        self.grade = grade
    
    def enroll_student(self, db):
        """Enroll student in course"""
        pass

    @staticmethod
    def update_grade(db, enrollment_id, grade):
        """Update grade for a student in a course"""
        pass
    
    @staticmethod
    def view_enrollments(db):
        """Fetch all enrollments with student, course details, and grade"""
        pass