pass_mark = 60
num_list = []
sentinel = -1
cut_off = 5

student_score = eval(input("What is the student score? "))
print("Student score is: ", student_score)

print("\nNow enter the scores for all other students in the class. When completed, enter '-1' to stop accepting input.")
number = eval(input("Enter a student's score: "))
while number != sentinel:
    num_list.append(number)
    number = eval(input("Enter another student's score: "))

# Sum scores of all students
students_grade = sum(num_list)

#add student's score to the other scores in the class to compute total class score
class_score = student_score + students_grade

# Compute class average
class_average_score = class_score / (len(num_list)+1)

# Compute class cut-off mark 
class_avgerage_cut = class_average_score - cut_off

# Print result -- conditional statement
if (student_score >= pass_mark) & (student_score >= class_avgerage_cut):
    print("\nPASSED! YOUR SCORE IS: ", student_score)
else:
    print("\nFAILED! YOUR SCORE IS: ", student_score)
