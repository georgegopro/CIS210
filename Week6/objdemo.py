"""" In-class demo of classes and objects """

class Person:
    def scream(self):
        print("AAAAAHH")
        

class Student(Person): 
    def __init__(self, name):
        self.name = name
        self.major = "CIS"
        
    def who_are_you(self):
        return self.name
    
    def change_major(self, new_major):
        self.major = new_major
        
    def whats_your_major(self):
        return self.major
        
class Teacher(Person):
    def __init__(self, name):
        self.name = name
        self.degree = "PhD"
    
    def  who_are_you(self):
        return "Professor " + self.name + " " +self.degree
        

        
nancy = Student("Nancy")
elizabeth = Student("Liz")
ted = Student("Theodore")
ted.change_major("English Architecture")

charley = Teacher("Charles")

people = [ nancy, ted, charley, elizabeth ]

for person in people:
    their_name = person.who_are_you()
    print(their_name)
    person.scream()
    
    

    

