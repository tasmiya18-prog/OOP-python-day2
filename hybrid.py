class Person:
    def __init__(self, name):
        self.name = name
    def display_person(self):
        print("Student Name:", self.name)
class Student(Person):
    def __init__(self, name, student_id):
        self.name = name               # ← direct call instead of super()
        self.student_id = student_id
    def display_student(self):
        print("Student ID:", self.student_id)
class SportsPlayer(Person):
    def __init__(self, name, sport_name):
        self.name = name              
        self.sport_name = sport_name
    def display_sports_player(self):
        print("Sports Name:", self.sport_name)
class CollegeStudent(Student, SportsPlayer):
    def __init__(self, college_name, name, student_id, sport_name):
        Student.__init__(self, name, student_id)
        SportsPlayer.__init__(self, name, sport_name)
        self.college_name = college_name
    def display_college_student(self):
        print("College Name:", self.college_name)
        self.display_person()
        self.display_student()
        self.display_sports_player()
college_student = CollegeStudent('BGS', 'Ria', 121, 'Badminton')
college_student.display_college_student()
