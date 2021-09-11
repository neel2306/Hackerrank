'''
TASK:
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

A Student class constructor, which has  parameters:
A string, .
A string, .
An integer, .
An integer array (or vector) of test scores, .
A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:
Grading.png
'''

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
        

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        count = 0
        for i in self.scores:
            count += i
        average = count / len(self.scores)
        if average < 40:
            return 'T'
        elif average >= 40 and average < 55:
            return 'D'
        elif average >= 55 and average < 70:
            return 'P'
        elif average >= 70 and average < 80:
            return 'A'
        elif average >= 80 and average < 90:
            return 'E'
        elif average >= 90 and average <= 100:
            return 'O'
            
