# creat a class called "student"
class Student(object):
    # define class attributes
    def __init__(self, name, major, portfolio_score, group_project_score, exam_score):
        self.name = name
        self.major = major
        self.portfolio_score = portfolio_score 
        self.group_project_score = group_project_score
        self.exam_score = exam_score

    def display_details(self):
        print(f"Name: {self.name}, Major: {self.major}, Self portfolio Score: {self.portfolio_score}, Group Project Score: {self.group_project_score}, Exam Score: {self.exam_score}")

# Create a Student object
# please input score marks out of 100 !!
student1 = Student("Coco", "BMI", 100, 100, 100)

# Call the display_details method to print the student's information
student1.display_details()