Student_name = input("What is the student name? ")
Student_score = int(input("insert the student score! "))
class_average_score = float(input("Please insert the class average! "))
minimum_score = class_average_score - 5
percentage = Student_score / 100 * 100
if (percentage >= 60) & (Student_score >= class_average_score):
    print(f"{Student_name} has passed the semsister with a score  {Student_score}, ")
else:
    print(f"{Student_score} is not a passing score. {Student_name} has failed this semister")
