PROPERTIES = ['StLastName', 'StFirstName', 'Grade', 'Classroom', 'Bus', 'GPA', 'TLastName', 'TFirstName']


def parse_data():
    file_data = []
    with open('students.txt', 'r') as file:
        for line in file:
            student_data = {}
            arr = line[:-1].split(',')
            for i, val in enumerate(arr):
                student_data[PROPERTIES[i]] = val
            file_data.append(student_data)
    return file_data


def filter_student(student_data, student_name, print_bus):
    for student in student_data:
        if student['StLastName'] == student_name:
            if print_bus:
                print(f'Last Name: {student["StLastName"]}\n'
                      f'First Name: {student["StFirstName"]}\n'
                      f'Bus Route: {student["Bus"]}\n')
            else:
                print(f'Last Name: {student["StLastName"]}\n'
                      f'First Name: {student["StFirstName"]}\n'
                      f'Grade: {student["Grade"]}\n'
                      f'Teacher Last Name: {student["TLastName"]}\n'
                      f'Teacher First Name: {student["TFirstName"]}\n'
                      f'Classroom: {student["Classroom"]}\n')


def filter_teacher(student_data, teacher_name):
    for student in student_data:
        if teacher_name == student['TLastName']:
            print(f'Last Name: {student["StLastName"]}\n'
                  f'First Name: {student["StFirstName"]}\n')


def filter_grade(student_data, grade):
    for student in student_data:
        if grade == student['Grade']:
            print(f'Last Name: {student["StLastName"]}\n'
                  f'First Name: {student["StFirstName"]}\n')


def filter_bus(student_data, bus):
    for student in student_data:
        if bus == student['Bus']:
            print(f'Last Name: {student["StLastName"]}\n'
                  f'First Name: {student["StFirstName"]}\n'
                  f'Grade: {student["Grade"]}\n'
                  f'Classroom: {student["Classroom"]}\n')


def filter_grade_high_low(student_data, grade, high_or_low):
    best_grade = None
    for student in student_data:
        if student['Grade'] == grade:
            if best_grade is None:
                best_grade = student
            elif high_or_low == 'H' and best_grade['GPA'] < student['GPA']:
                best_grade = student
            elif high_or_low == 'L' and best_grade['GPA'] > student['GPA']:
                best_grade = student
    print(f'Last Name: {best_grade["StLastName"]}\n'
          f'First Name: {best_grade["StFirstName"]}\n'
          f'GPA: {best_grade["GPA"]}\n'
          f'Teacher: {best_grade["TLastName"]}\n'
          f'Bus Route: {best_grade["Bus"]}\n')


def compute_average(student_data, grade):
    # Add error checking if no students are found
    total = 0.0
    num = 0
    for student in student_data:
        if student['Grade'] == grade:
            num += 1
            total += float(student['GPA'])
    average = total / num
    print(f'Average GPA for students with a grade of {grade}: {average}\n')


def compute_info(student_data):
    # Stores the number of students per grade
    number_of_students = [0, 0, 0, 0, 0, 0, 0]
    for student in student_data:
        number_of_students[int(student['Grade'])] += 1
    for i, count in enumerate(number_of_students):
        print(f'{i}: {count}')


if __name__ == '__main__':
    students_data = parse_data()    
    while True:
        user_input = input("Enter a command: ")
        arr = user_input.split(' ')
        # print(arr)
        if arr[0][0] == "S":
            if len(arr) == 3:
                filter_student(students_data, arr[1], True)
            else:
                filter_student(students_data, arr[1], False)
        elif arr[0][0] == "T":
            filter_teacher(students_data, arr[1])
        elif arr[0][0] == "B":
            filter_bus(students_data, arr[1])
        elif arr[0][0] == "G":
            if len(arr) == 2:
                filter_grade(students_data, arr[1])
            if len(arr) == 3:
                filter_grade_high_low(students_data, arr[1], arr[2][0])
        elif arr[0][0] == "A":
            compute_average(students_data, arr[1])
        elif arr[0][0] == "I":
            compute_info(students_data)
        if arr[0][0] == 'Q':
            break

# print("S[tudent]: <lastname> [B[us]]\n"
#                   "T[eacher]: <lastname>\n"
#                   "B[us]: <number>\n"
#                   "G[rade]: <number> [H[igh]|L[ow]]\n"
#                   "A[verage]: <number>\n"
#                   "I[nfo]\n"
#                   "Q[uit]\n")
