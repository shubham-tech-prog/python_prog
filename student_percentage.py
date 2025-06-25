
# Homework -: Student has features like name , roll no and subject with marks .there are 5 subject for every student with some marks .
#              Student has one operation which will display percentage of student

# (use dictionary for subject and marks)



# Define Student class
class Student:
    # Function to display percentage
    def display_percentage(self):
        total = sum(self.marks.values())     # Sum of marks
        percentage = total / len(self.marks) # Calculate percentage
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)
        print("Percentage:", percentage, "%")


# Create object
s1 = Student()

# Assign details
s1.name = "Shubham"
s1.roll_no = 21

# Dictionary for subject and marks
s1.marks = {
    "Math": 91,
    "Science": 88,
    "English": 92,
    "History": 95,
    "Computer": 90
}

# Call function to display percentage
s1.display_percentage()
