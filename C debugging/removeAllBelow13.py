class Student:
    def __init__(self, age):
        self.age = age

# def remove_all_below_13(students):
#     for i in range(len(students)):
#         if students[i].age < 13:
#             students.pop(i)  # Removes the student at index i


def remove_all_below_13(students: list):

    for i in range(len(students)-1, -1, -1):  # start from end instead to avoid errors
        if students[i].age < 13:
            students.pop(i)


# Example usage
students = [Student(15), Student(10), Student(12), Student(14)]
remove_all_below_13(students)

for student in students:
    print(student.age)
