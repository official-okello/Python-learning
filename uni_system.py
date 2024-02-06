class School:
    def welcome():
        print('Welcome to this system...')
class Professor:
    def __init__(self,full_name,subject):
        self.name = full_name
        self.subject = subject
    def grade_student(self):
        pass
    def send_message(self,student,message):
        print(f'Student: {self.student} has received the message {self.message}')
class Student:
    def __init__(self,full_name):
        self.name = full_name
    def enroll_subject(self):
        pass
class Subject:
    def add_new(self,title):
        with open('subjects.txt','a') as file:
            file.write('\r' + title)